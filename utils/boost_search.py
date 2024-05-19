import threading


#  This method to increase speed for back test by using threads
#  This link in linkedin talks about using threads in this code :
#  https://www.linkedin.com/posts/abd-alftah-salem-a3ba0b1bb_%D9%83%D9%86%D8%AA-%D8%A7%D9%84%D9%8A%D9%88%D9%85-%D8%B4%D8%BA%D8%A7%D9%84-%D8%B9%D9%84%D9%89-%D8%A8%D8%B1%D9%88%D8%AC%D9%8A%D9%83%D8%AA-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-%D9%83%D9%86%D8%AA-%D8%A8%D8%AC%D8%B1%D8%A8-activity-7072175553000222720-uYA1?utm_source=share&utm_medium=member_desktop

def boost_back_test(callback, input_tickers, interval, strategy_name):
    try:
        thread_list = []
        for ticker in input_tickers:
            th = threading.Thread(target=callback,
                                  args=(ticker, interval, strategy_name))
            thread_list.append(th)
            th.start()

        for thread in thread_list:
            thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")


def boost_search(callback, assets, interval, limit=1000):
    try:
        thread_list = []
        for i in range(len(assets)):
            th = threading.Thread(target=callback, args=(assets[i], interval, limit))
            thread_list.append(th)
            th.start()

        for thread in thread_list:
            thread.join()



    except:
        pass
