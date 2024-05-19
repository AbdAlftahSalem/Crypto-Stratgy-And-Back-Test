<img src="assets/images/logo.png" width="300"/>

Strategy And Backtest Crypto Algorithm
======================================

This repository contains a Python-based strategy and backtesting algorithm for cryptocurrency trading. The strategy is
built using Python with the option to incorporate additional algorithms.

Description
-----------

The purpose of this project is to provide an open-source solution for building and backtesting cryptocurrency trading
strategies. The complete code for the backtest and the indicators will be published, allowing users to use and modify it
as needed.


Features
--------

- Retrieves price data from the Binance API .
- Collection of indicators code .
- Performs backtesting for the algorithms .
- Template backtest for any algorithm .
- Supports short and long positions .
- Supports static or dynamic TP or SL.
- Allows for customization of the strategy and backtest .
- Saves data, backtest results, and applies the algorithm .
- Automatic to start analyze market and send signals to telegram .
- Convert df from 5m interval to 15m and 30m to speed up code .
- Show result for any algorithm in any time .
- Save backtest signal and data in local device .

How to Use
----------

Please follow the steps below to use this algorithms:

1. Read the comments in the code to understand the implementation details and adjust them as necessary.
2. Clone the repository by running the following command:

```bash
git clone https://github.com/AbdAlftahSalem/Crypto-Stratgy-And-Back-Test.git
```

3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

1. In the `const_app.py` file, specify whether you want to retrieve data from Binance or use local CSV data for the
   backtest. If retrieving data, provide the necessary API credentials.
2. Specify the tickers you want to analyze in the `const_app.py` file.
3. Specify the intervals you want to analyze in the `const_app.py` file.
4. Specify the folder where you want to save the data in the `const_app.py` file.
5. Specify the take profit value for all intervals in the `const_app.py` file.
6. Specify the stop loss value in the `const_app.py` file. The stop loss value will be divided by the take profit
   percentage.
7. Execute the code and observe the backtest results and generated outputs.

Feel free to explore and customize the code to suit your specific needs and trading strategies.

System Strategies
----------
<h3> NE strategy ( Dynamic TP / SL )</h3>

- The strategy provided Short and long position .
- Number of all long signals : 5333
- Number of win long signals : 4067
- Number of lose long signals : 1266
- Summation of PCT for win signals : 8228.91 %
- Summation of PCT for lose signals : -2042 %
- PCT success for long signals : 76.62 %

------------------------------------------------

- Number of all short signals : 4699
- Number of win short signals : 3688
- Number of lose short signals : 1011
- Summation of PCT for win signals : 5813.17 %
- Summation of PCT for lose signals : -1303.71 %
- PCT success for short signals : 78.48 %

<h3> NE strategy ( Static TP / SL )</h3>

- The strategy provided Short and long position .
- Number of all long signals : 6009
- Number of win long signals : 4313
- Number of lose long signals : 1400
- Summation of PCT for win signals : 6009.0 %
- Summation of PCT for lose signals : -1356.75 %
- PCT success for long signals : 75.49 %

------------------------------------------------

- Number of all short signals : 4771
- Number of win short signals : 3688
- Number of lose short signals : 1083
- Summation of PCT for win signals : 5206.0 %
- Summation of PCT for lose signals : -1023.68 %
- PCT success for short signals : 77.3 %

<h3> SAR strategy ( Dynamic TP / SL )</h3>

- Number of all long signals : 4771
- Number of win long signals : 15893
- Number of lose long signals : -6555
- Summation of PCT for win signals : 11535.76 %
- Summation of PCT for lose signals : -5462.79 %
- PCT success for long signals : 58.76 %

<h3> SAR strategy ( Static TP / SL )</h3>

- Number of all long signals : 42930
- Number of win long signals : 26443
- Number of lose long signals : -16487
- Summation of PCT for win signals : 16943.0 %
- Summation of PCT for lose signals : -6986.83 %
- PCT success for long signals : 61.6 %

------------------------------------------------
<h3> VS strategy ( Dynamic TP / SL )</h3>

- Number of all long signals : 27396
- Number of win long signals : 15683
- Number of lose long signals : 11713
- Summation of PCT for win signals : 19179.53 %
- Summation of PCT for lose signals : -9808.65 %
- PCT success for long signals : 57.25 %

<h3> VS strategy ( Static TP / SL )</h3>

- Number of all long signals : 42930
- Number of win long signals : 26443
- Number of lose long signals : 16487
- Summation of PCT for win signals : 16943.0 %
- Summation of PCT for lose signals : -6986.83 %
- PCT success for long signals : 61.6 %

Contributing
------------

Contributions to this project are welcome. If you have any ideas, suggestions, or improvements, please feel free to open
an issue or submit a pull request. Your contributions can help enhance the functionality and effectiveness of this
strategy and backtesting algorithm.

When contributing, please ensure to follow the existing code style and guidelines.

Contact with me
---------------

[Whats App]()<br>
[LinkedIn]()<br>
[Telegram](https://t.me/Abd_Alftah_Al_shanti)



License
-------

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of
this license.

Please note that while this project provides a strategy and backtesting algorithm, it does not guarantee profitable
trading or financial success. Use the code and strategy at your own risk and discretion.

If you find this project helpful or use it as a basis for your work, attribution would be appreciated but is not
required.

Happy trading and backtesting!

