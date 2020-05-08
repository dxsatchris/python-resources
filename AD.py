#from ldap3 import Server, Connection, ALL
import ldap3
LDAP_USER = 'XXXXXXXXXXXXXXXX'
LDAP_PWD = 'k@4Uq54(5YgJ+'
LDAP_DOMAIN= 'XXXXXX'
total_entries = 0

class ldapipl:


server = ldap3.Server('tetsuo')
conn = ldap3.Connection(server, user= LDAP_DOMAIN + "\\" + LDAP_USER, password = LDAP_PWD, authentication='NTLM')
conn.bind()
if not conn.bind():
    print('error in bind', conn.result)
print conn
"""conn.search(search_base = 'CN=Users,DC=XXXXXX,DC=COM',
	search_filter = '(objectClass=user)',
	search_scope = 'SUBTREE',
	attributes = ['cn', 'givenName','objectClass'],
	paged_size = 50)
total_entries += len(conn.response)
for entry in conn.response:
	try :
		print entry['dn']
	except:
		print "--" + str(entry['dn'].encode("iso-8859-1" ))
	print entry['attributes']

cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
while cookie:
	conn.search(search_base = 'CN=Users',
		search_filter = '(objectClass=user)',
		search_scope = 'SUBTREE',
		attributes = ['cn', 'givenName','objectClass'],
		paged_size = 50,
		paged_cookie = cookie)
	total_entries += len(conn.response)
	cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
	for entry in conn.response:
		try :
			print entry['dn']
		except:
			print "--" + str(entry['dn'].encode("iso-8859-1" ))
		print entry['attributes']
print('Total entries retrieved:', total_entries)

#conn.add('cn=testpython,cn=users,dc=xxxxxxx,dc=com', ['top','person','organizationalPerson','user'], {'sn': 'Young'})
conn.add('cn=testpython,cn=users,dc=xxxxxxx,dc=com', ['top','group'])"""

if conn.search('CN=Thierry ETA,CN=Users,DC=xxxxxxx,DC=com', '(objectclass=person)'):
	print 'ok'
else :
	print 'pas ok'

print(conn.result)

# close the connection

conn.unbind()