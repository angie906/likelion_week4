cookies={'탱커':'우유맛쿠키',
'딜러':'칠리맛쿠키',
'힐러':'천사맛쿠키',
'서포터':'석류맛쿠키'}

print("바꾸기 전 coockies: ",cookies)

for cookie in cookies:
    if cookie=='탱커':
        cookies[cookie]='다크초코맛쿠키'
    elif cookie=='딜러':
        cookies[cookie]='라떼맛쿠키'
    elif cookie=='힐러':
        cookies[cookie]='허브맛쿠키'

print("바꾼 후 coockies: ",cookies)