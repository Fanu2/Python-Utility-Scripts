html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Report</title>
</head>
<body>
    <h1>Report Title</h1>
    <p>This is a sample report.</p>
</body>
</html>
'''

with open('report.html', 'w') as file:
    file.write(html_content)
