# SSDeep TEST ON EMAILS
import re
import email_walk as walk
import os


def strip_urls_from_message(filename):
    """
        Takes in a file, subs urls with nothing. Then writes this data to
        a different file with 2 in front of the file name.
    """

    message = walk.walk_email_body(filename)
    #stripping links and links completely even TLD
    #message = re.sub('<https?:\/\/.+>', '', message)  # removes links such as (https)
    #message = re.sub('\[https?:\/\/.+\]', '', message) #removes links such as [https]

    #stripping links partially up to TLD
    # message = re.sub('\[', '', message)
    # message = re.sub('[^m:\/\/]\/.+', '', message)
    # message = os.linesep.join([s for s in message.splitlines() if s])

    file = open('2' + filename, 'w')
    file.write(message)
    file.close()


def load_path_with_os():
    """Checks for the correct OS and changes the assets variable
    to match for the correct operating system syntax"""

    if os.name == 'mac' or 'linux':
        assets = "./assets"
    elif os.name == 'nt':
        assets = ".\\assets"

    return os.chdir(assets)


def header_combination(filename):
    """
        Takes in a file, combines the data from the headers
        and concats them into one long string
        arguments include headers['to,from,subject']
        and a lot more must look at email module.
        i.e: print 'to: ', headers['to']
    """

    headers = walk.walk_email_headers(filename)
    header2 = (headers['to'] + headers['from'] + headers['subject'] +
               headers['mime-version'] + headers['message-id'])

    file = open('2' + filename + '.txt', 'w')
    file.write(header2)
    file.close()


def run():
    load_path_with_os()

    # section to run strip url function with all files in assets directory
    for filename in os.listdir(os.getcwd()):
        strip_urls_from_message(filename)

    # section to run to get the headers and combine them creating a new file
    # for filename in os.listdir(os.getcwd()):
    #     header_combination(filename)



if __name__ == "__main__":
    # all this to be put in run method later
    run()
