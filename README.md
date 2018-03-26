# g45g23r
Run api and reload on change
```
gunicorn --reload transactions_api.app:app

```
Run __main__.py as module

```angular2html
gunicorn transactions_api.__main__:main
```


## Routes
* **GET**  /transactions
* **GET**  /transactions/<GUID>
* **GET**  /transactions/wallet/btc/<ADDRESS>
* **GET**  /transactions/wallet/eth/<ADDRESS>
* **POST** /trasactions/wallet/btc
* **POST** /trasactions/wallet/eth
* **GET**  /account/wallet/btc/<ADDRESS>
* **GET**  /account/wallet/eth/<ADDRESS>

