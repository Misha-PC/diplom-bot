import psycopg2
from accessify import private
from datetime import datetime
from utilities_func import readConfig
from utilities_func import slugify
from utilities_func import dump



class Database(object):
    params = None
    db = dict()

    def __init__(self, params=None):
        if isinstance(params, str):
            """ if conn == file patch """
            config = readConfig(params)
            if not config:
                raise Exception("read DB config error ")

            try:
                self.params = config['postgresql']
            except Exception as error:
                raise Exception(error)

        elif isinstance(params, dict):
            """ if conn == raw connection data """
            self.params = params

        else:
            """ undefined conn """
            raise Exception("DB connection fail! Undefined connection data!")

        self.connect()

    @private
    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self.params)

        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    def get_sites(self, member=None, slug=None, id_=None):

        query = "SELECT * from site"
        if id_:
            query += " where  id='{}'".format(str(id_))

        elif slug:
            query += " where  slug='{}'".format(str(slug))

        elif member:
            query += " where  member_id='{}'".format(str(member))

        cur = self.conn.cursor()
        cur.execute(query)

        sites = cur.fetchall()
        cur.close()
        return sites

    def add_site(self,
                 member_id=None,
                 title=None,
                 head=None,
                 body=None,
                 side_bar=None,
                 style="Style1",
                 pattern="Site"
                 ):
        val = dict()
        val_n = str()
        val_d = str()

        val['member_id'] = str(member_id)
        if title:
            val['title'] = title
            val['slug'] = slugify(title)

        if head:
            val['head'] = head

        if body:
            val['body'] = dump(body)

        if side_bar:
            val['side_bar'] = dump(side_bar)

        val['style'] = style
        val['pattern'] = pattern

        slug_f = self.get_sites(slug=val["slug"])

        while slug_f:
            val['slug'] += '-'
            slug_f = self.get_sites(slug=val["slug"])

        # val['create'] = datetime.now()
        val['last_update'] = datetime.now()

        for n, d in val.items():
            val_n += '{}, '  .format(n)
            val_d += "'{}', ".format(d)

        val_n = val_n[:-2]
        val_d = val_d[:-2]

        query = "INSERT INTO site "
        query += "({}) ".format(val_n)
        query += "values ({});".format(val_d)

        print(query)

        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        cur.close()

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

