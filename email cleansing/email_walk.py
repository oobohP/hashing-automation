import email


def walk_email_body(file_name):
    """Takes in an .eml file, opens it and walks through
        the file in order to get the body text of the email
        the string object is converted to unicode and returned"""

    body = ''  # is cleared everytime function is run

    file = open(file_name, 'r')
    email_file = email.message_from_file(file)
    file.close()

    try:
        if email_file.is_multipart():
            for part in email_file.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)
                    break
        else:
            body = email_file.get_payload(decode=True)
    except IOError:
        print 'file does not exist'

    #  convert string to unicode before sending it out
    charset = email_file.get_content_charset('iso-8859-1')  # fall back
    body = body.decode(charset, 'unicode')

    return body  # unicode string


def walk_email_headers(file_name):
    """Takes in a file walks through it and returns everything in
        a dictionary format optional to return as either a string"""

    headers = email.Parser.Parser().parse(open(file_name, 'r'))

    return headers
