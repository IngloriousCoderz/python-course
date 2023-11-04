import re

re.findall(r'^[\w\.]+@\w+\.\w{2,3}$', 'antony.mistretta@gmail.com') #?

re.sub(r'\sand\s', ' & ', 'Monsters And Co.', flags=re.IGNORECASE) #?

'JavaScript is awesome!'.replace('JavaScript', 'Python') #?
'Monsters And Co.'.replace(' And ', ' & ') #?
'Andalusia And Co.'.replace('And', '&') #?
'Andalusia And Co.'.replace(' And ', ' & ') #?
