import webbrowser

while True:
    username = input("Write down your github user name, to open stats about your account.\n")

    url = 'https://github-readme-stats.vercel.app/api/top-langs/?username=' + username + '&layout=compact'
    url_2 = 'https://github-readme-stats.vercel.app/api?username=' + username + '&hide=contribs,prs&theme=tokyonight'
    webbrowser.open(url)
    webbrowser.open(url_2)
