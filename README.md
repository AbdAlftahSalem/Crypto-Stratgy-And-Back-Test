Strategy And Backtest Crypto Algorithm
======================================

This repository contains a Python-based strategy and backtesting algorithm for cryptocurrency trading. The strategy is
built using Python and relies on two primary indicators, with the option to incorporate additional algorithms. The first
indicator used is the Nadaraya-Watson Envelope [LuxAlgo], followed by VWAP (Volume-Weighted Average Price) and EMA (
Exponential Moving Average).

Description
-----------

The purpose of this project is to provide an open-source solution for building and backtesting cryptocurrency trading
strategies. The complete code for the backtest and the indicators will be published, allowing users to use and modify it
as needed.

Backtest Output
--------------
This is the output search from 1 Jan 2022 to 10 Jul 2023


<img src="assets/ETHUSDT-30m-long.svg" alt="Backtest Output" width="100%">

Features
--------

- Retrieves price data from the Binance API.
- Calculates the Nadaraya-Watson Envelope [LuxAlgo].
- Calculates VWAP.
- Calculates EMA.
- Performs backtesting for the algorithm.
- Supports both short and long positions.
- Allows for customization of the strategy.
- Saves data, backtest results, and applies the algorithm.

How to Use
----------

Please follow the steps below to use this algorithm:

1. Read the comments in the code to understand the implementation details and adjust them as necessary.
2. Clone the repository by running the following command:

```bash
git clone https://github.com/AbdAlftahSalem/Crypto-Stratgy-And-Back-Test.git
```

3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```


4. In the `const_app.py` file, specify whether you want to retrieve data from Binance or use local CSV data for the backtest. If retrieving data, provide the necessary API credentials.
5. Specify the tickers you want to analyze in the `const_app.py` file.
6. Specify the intervals you want to analyze in the `const_app.py` file.
7. Specify the folder where you want to save the data in the `const_app.py` file.
8. Specify the take profit value for all intervals in the `const_app.py` file.
9. Specify the stop loss value in the `const_app.py` file. The stop loss value will be divided by the take profit percentage.
10. Execute the code and observe the backtest results and generated outputs.

Feel free to explore and customize the code to suit your specific needs and trading strategies.

Contributing
------------

Contributions to this project are welcome. If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request. Your contributions can help enhance the functionality and effectiveness of this strategy and backtesting algorithm.

When contributing, please ensure to follow the existing code style and guidelines.

License
-------

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of this license.

Please note that while this project provides a strategy and backtesting algorithm, it does not guarantee profitable trading or financial success. Use the code and strategy at your own risk and discretion.

If you find this project helpful or use it as a basis for your work, attribution would be appreciated but is not required.

Happy trading and backtesting!

