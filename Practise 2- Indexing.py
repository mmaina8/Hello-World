Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first_name='Joy'
>>> last_name='Wahome'
>>> school='AkiraChix'
>>> 'Hello,my name is'+' '+first_name+' '+last_name+'.'+'I go to'+' '+school
'Hello,my name is Joy Wahome.I go to AkiraChix'
>>> occupation='student'
>>> age='20'
>>> home='Karen'
>>> message='My name is {} {}. I am {} years old and I live in {}. I am a {} at {}.'.format(first_name,last_name,age,home,occupation,school)
>>> message
'My name is Joy Wahome. I am 20 years old and I live in Karen. I am a student at AkiraChix.'
>>> message='My name is {} {}.\n I am {} years old and I live in {}.\n I am a {} at {}.'.format(first_name,last_name,age,home,occupation,school)
>>> print (message)
My name is Joy Wahome.
 I am 20 years old and I live in Karen.
 I am a student at AkiraChix.
>>> message='My name is {} {}. \n I am {} years old and I live in {}. \n I am a {} at {}.'.format(first_name,last_name,age,home,occupation,school)
>>> print (message)
My name is Joy Wahome. 
 I am 20 years old and I live in Karen. 
 I am a student at AkiraChix.
>>> I am a student at AkiraChix.
SyntaxError: invalid syntax
>>> message
'My name is Joy Wahome. \n I am 20 years old and I live in Karen. \n I am a student at AkiraChix.'
>>> message='My name is {first_name} {last_name}.\n I am {first_name} years old and I live in {home}.\n I am a {occupation} at {school}.'.format(first_name=first_name,last_name=last_name,age=age,home=home,occupation=occupation,school=school)
>>> message
'My name is Joy Wahome.\n I am Joy years old and I live in Karen.\n I am a student at AkiraChix.'
>>> print (message)
My name is Joy Wahome.
 I am Joy years old and I live in Karen.
 I am a student at AkiraChix.
>>> f 'Hello {first_name}, you are {age}'
SyntaxError: invalid syntax
>>> message2=f 'Hello {first_name}, you are {age}'
SyntaxError: invalid syntax
>>> messagetwo=f 'Hello {first_name}, you are {age}'
SyntaxError: invalid syntax
>>> f"{2 * 37}"
'74'
>>> messagetwo= f'Hello {first_name}, you are {age}'
>>> print (message)
My name is Joy Wahome.
 I am Joy years old and I live in Karen.
 I am a student at AkiraChix.
>>> print(message)
My name is Joy Wahome.
 I am Joy years old and I live in Karen.
 I am a student at AkiraChix.
>>> print (messagetwo)
Hello Joy, you are 20
>>> mom='Janie"
SyntaxError: EOL while scanning string literal
>>> mom='Janie'
>>> sister='Ivy'
>>> bf='Stuart'
>>> friend='Maripet'
>>> bro='Trevor'
>>> f2='Penninah'
>>> text=f'I love the people in my life. \n My {mom},{sister} and {bf} are extra special. They keep me going through each day.\n I love my friends as well; {friend},{bro} and {f2}.'
>>> text
'I love the people in my life. \n My Janie,Ivy and Stuart are extra special. They keep me going through each day.\n I love my friends as well; Maripet,Trevor and Penninah.'
>>> print(text)
I love the people in my life. 
 My Janie,Ivy and Stuart are extra special. They keep me going through each day.
 I love my friends as well; Maripet,Trevor and Penninah.
>>> text=f'\t I love the people in my life. \n My {mom},{sister} and {bf} are extra special. They keep me going through each day.\n I love my friends as well; {friend},{bro} and {f2}.'
>>> print (text)
	 I love the people in my life. 
 My Janie,Ivy and Stuart are extra special. They keep me going through each day.
 I love my friends as well; Maripet,Trevor and Penninah.
>>> type (mom)
<class 'str'>
>>> type (age)
<class 'str'>
>>> age=20
>>> type (age)
<class 'int'>
>>> 
>>> 
>>> first_name='Joy'
>>> first_name='James'
>>> first_balance='1000'
>>> second_name='Jane'
>>> second_balance=10000
>>> sms='Hello {},\n your balance is 1000'
>>> print (sms)
Hello {},
 your balance is 1000
>>> sms='Hello {},\n your balance is {}'.format(first_name,first_balance)
>>> print (sms)
Hello James,
 your balance is 1000
>>> sms2='Hello {},\n your balance is {}'.format(second_name,second_balance)
>>> print (sms2)
Hello Jane,
 your balance is 10000
>>> print (sms)'\t' (sms2)
SyntaxError: invalid syntax
>>> s='AkiraChix'
>>> s.upper ()
'AKIRACHIX'
>>> s.lower()
'akirachix'
>>> s.capitalize()
'Akirachix'
>>> s.endswith('x')
True
>>> s.endswith('k')
False
>>> s.sartswith('x')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.sartswith('x')
AttributeError: 'str' object has no attribute 'sartswith'
>>> s.startswith('x')
False
>>> s.startswith('a')
False
>>> s.startswith('A')
True
>>> s.islower()
False
>>> s.isupper()
False
>>> s.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'
>>> b=s.islower()
>>> b.islower()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b.islower()
AttributeError: 'bool' object has no attribute 'islower'
>>> b=s.lower()
>>> b.islower()
True
>>> b.isupper()
False
>>> b.isalpha()
True
>>> b.isalnum()
True
>>> s.replace('x','z')
'AkiraChiz'
>>> s.replace('x','z')
'AkiraChiz'
>>> s.replace('z','x')
'AkiraChix'
>>> s.replace('a','b')
'AkirbChix'
>>> s.replace('b','a')
'AkiraChix'
>>> s[0]
'A'
>>> s[3]
'r'
>>> s[]
SyntaxError: invalid syntax
>>> s[9]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s[9]
IndexError: string index out of range
>>> s[-9]
'A'
>>> len(s)
9
>>> s[0:4]
'Akir'
>>> s[5:8]
'Chi'
>>> s[5:9]
'Chix'
>>> s[5:10]
'Chix'
>>> s[3:]
'raChix'
>>> s[:4]
'Akir'
>>> s[-9:-6]
'Aki'
>>> s[-9:-5]
'Akir'
>>> s[0:4]==s[-9:-5]
True
>>> s[-4:-1]
'Chi'
>>> s[3:]==s[:-6]
False
>>> s[3:]==s[-6:]
True
>>> s[:4]==s[-5]
False
>>> s[:4]==s[:-5]
True
>>> first_name='Joy'
>>> second_name='Wahome'
>>> full_name='{} {}'.format(first_name,second_name)
>>> full_name
'Joy Wahome'
>>> len(first_name)
3
>>> len(last_name)
6
>>> first_name=[3]
>>> first_name=[1]
>>> a=full_name[0:4]
>>> b=full_name[4:10]
>>> a==first_name
False
>>> a=full_name[0:3]
>>> b=full_name[4:9]
>>> a==first_name
False
>>> a=full_name[0: ]
>>> a
'Joy Wahome'
>>> a=full_name[0: ]
>>> a=full_name[0:2]
>>> a
'Jo'
>>> a=full_name[0:3]
>>> a
'Joy'
>>> a==first_name
False
>>> first_name
[1]
>>> 
>>> 
>>> first_name='Joy"
SyntaxError: EOL while scanning string literal
>>> 
>>> first_name='Joy'
>>> last_name='Wahome'
>>> full_name='{} {}'.format(first_name,last_name)
>>> a=full_name[0:3]
>>> a==first_name
True
>>> b=full_name[4:9]
>>> b==second_name
False
>>> b=full_name[3:9]
>>> b==second_name
False
>>> b=full_name[4:]
>>> b==second_name
True
>>> b=full_name[4:10]b==second_name
SyntaxError: invalid syntax
>>> b=full_name[4:10]
>>> b==second_name
True
>>> 
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> help(symbols)
No Python documentation found for 'help(symbols)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          atexit              http                scrolledlist
__main__            audioop             hyperparser         search
_abc                autocomplete        idle                searchbase
_ast                autocomplete_w      idle_test           searchengine
_asyncio            autoexpand          idlelib             secrets
_bisect             base64              imaplib             select
_blake2             bdb                 imghdr              selectors
_bootlocale         binascii            imp                 setuptools
_bz2                binhex              importlib           shelve
_codecs             bisect              inspect             shlex
_codecs_cn          browser             io                  shutil
_codecs_hk          builtins            iomenu              signal
_codecs_iso2022     bz2                 ipaddress           site
_codecs_jp          cProfile            itertools           smtpd
_codecs_kr          calendar            json                smtplib
_codecs_tw          calltip             keyword             sndhdr
_collections        calltip_w           lib2to3             socket
_collections_abc    cgi                 linecache           socketserver
_compat_pickle      cgitb               locale              sqlite3
_compression        chunk               logging             squeezer
_contextvars        cmath               lzma                sre_compile
_csv                cmd                 macosx              sre_constants
_ctypes             code                macpath             sre_parse
_ctypes_test        codecontext         mailbox             ssl
_datetime           codecs              mailcap             stackviewer
_decimal            codeop              mainmenu            stat
_dummy_thread       collections         marshal             statistics
_elementtree        colorizer           math                statusbar
_functools          colorsys            mimetypes           string
_hashlib            compileall          mmap                stringprep
_heapq              concurrent          modulefinder        struct
_imp                config              msilib              subprocess
_io                 config_key          msvcrt              sunau
_json               configdialog        multicall           symbol
_locale             configparser        multiprocessing     symtable
_lsprof             contextlib          netrc               sys
_lzma               contextvars         nntplib             sysconfig
_markupbase         copy                nt                  tabnanny
_md5                copyreg             ntpath              tarfile
_msi                crypt               nturl2path          telnetlib
_multibytecodec     csv                 numbers             tempfile
_multiprocessing    ctypes              opcode              test
_opcode             curses              operator            textview
_operator           dataclasses         optparse            textwrap
_osx_support        datetime            os                  this
_overlapped         dbm                 outwin              threading
_pickle             debugger            paragraph           time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple formatter           pydoc_data          weakref
_testmultiphase     fractions           pyexpat             webbrowser
_thread             ftplib              pyparse             window
_threading_local    functools           pyshell             winreg
_tkinter            gc                  query               winsound
_tracemalloc        genericpath         queue               wsgiref
_warnings           getopt              quopri              xdrlib
_weakref            getpass             random              xml
_weakrefset         gettext             re                  xmlrpc
_winapi             glob                redirector          xxsubtype
abc                 grep                replace             zipapp
aifc                gzip                reprlib             zipfile
antigravity         hashlib             rlcompleter         zipimport
argparse            heapq               rpc                 zlib
array               help                rstrip              zoomheight
ast                 help_about          run                 zzdummy
asynchat            history             runpy               
asyncio             hmac                runscript           
asyncore            html                sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
