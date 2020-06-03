def set_docker_proxy(self, proxy_url=None):
    self.logger.info(
        'Setting docker proxy to {proxy_url}'.format(
            proxy_url=proxy_url,
        )
    )

    direct_conf = '''
http_port 127.0.0.1:3128
http_access allow all
cache deny all
dns_v4_first on
'''
    through_auth_proxy = '''
cache_peer {hostname} parent {port} 0 default no-query login={username}:{password}

acl all src 0.0.0.0/0
never_direct allow all
http_access allow all

http_port 127.0.0.1:3128
cache deny all
dns_v4_first on
'''
    through_direct_proxy = '''
cache_peer {hostname} parent {port} 0 default no-query

acl all src 0.0.0.0/0
never_direct allow all
http_access allow all

http_port 127.0.0.1:3128
cache deny all
dns_v4_first on
'''

def get_keyboard_proximity_table(
    self,
    keyboard_layout=qwerty_layout,
):
    close_chars_table = collections.defaultdict(set)
    for row in range(len(keyboard_layout)):
        for col in range(len(keyboard_layout[row])):
            curr_char = keyboard_layout[row][col]
            for close_char_relative_row in (-1, 0, 1):
                for close_char_relative_col in (-1, 0, 1):
                    if abs(close_char_relative_row + close_char_relative_col) == 2:
                        continue

                    adj_char_row = row + close_char_relative_row
                    adj_char_col = col + close_char_relative_col
                    if adj_char_row < 0 or adj_char_col < 0:
                        continue

                    try:
                        adjecent_char = keyboard_layout[adj_char_row][adj_char_col]
                    except IndexError:
                        continue

                    if adjecent_char != curr_char:
                        close_chars_table[curr_char].add(adjecent_char)
    return close_chars_table


@cherrypy.expose
@cherrypy.tools.json_out()
class StringGeneratorWebService:
    frontend_db_servers = [
        'intsights-frontend-us-database-shard-1',
    ]

    async def update_rates(
        self,
    ):
        while True:
            pass


profile_model.latest_posts_datetime = [
    datetime.datetime.utcnow() - datetime.timedelta(
        days=10,
    ),
    datetime.datetime.utcnow() - datetime.timedelta(
        days=12,
    ),
]
