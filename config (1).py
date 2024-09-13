from configparser import ConfigParser
config_object = ConfigParser()

config_object['DEBUG FLAG'] = {
    "debug": "False"
}

config_object['LOG FILE DETAILS'] = {
    "success": "/Users/shreejakatama/Downloads/Internship/Folder Code/Log File Success.txt",
    "exceptions": "/Users/shreejakatama/Downloads/Internship/Folder Code/Log File Exceptions.txt"
}

config_object['RTF TAGS'] = {
    "page break": "\\endnhere",
    "header": "\\header",
    "title": "\\trhdr",
    "row start": "\\trowd",
    "row end": "\\row",
    "cell end": "\\cell}"
}
config_object['RE EXPRESSIONS'] = {
    "font table": r"{\\fonttbl(.*)}",
    "font pattern": r'{\\f(\d+)\\.*? ([^;]+?);}',
    "colour pattern": r"\\red(\d+)\\green(\d+)\\blue(\d+);",
    "header": r"{(?!\\)(.+)\\cell}",
    "headerstyle": r"(?<=q)[lrc]\\",
    "styles": r"\\(f\d+)\\(fs\d+)\\(cf\d+)"

}
config_object['HEADER ALIGNMENT'] = {
    "l": "left",
    "c": "centre",
    "r": "right"
}
config_object['RTF STYLE TAGS'] = {
    "bold":"\\b\\",
    "italic":"\\i\\",
    "underline":"\\ul\\",
    "superscript":"\\super\\",
    "subscript":"\\sub\\",

}

with open('config.ini', 'w') as conf:
    config_object.write(conf)