from polygon import RESTClient
import config 

def main():

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(config.key) as client:
        resp = client.stocks_equities_daily_open_close("AAPL", "2021-06-11")
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()