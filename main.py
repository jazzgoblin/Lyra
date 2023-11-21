from keyword_recognizer import listen_for_keyword


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    live = True
    times_ran = 1
    while live is True:
        print("This is attempt number " + str(times_ran))
        listen_for_keyword()
        times_ran = times_ran + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
