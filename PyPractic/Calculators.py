import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self, date=None):
        today_stats = 0
        if not date:
            date = dt.date.today()
        for item in self.records:
            if item.date == date:
                today_stats += item.amount
        return today_stats

    def get_week_stats(self, date=None):
        if not date:
            date = dt.date.today()
        else:
            date = dt.datetime.strptime(date, '%d.%m.%Y')
            date = dt.datetime.date(date)
        week_ago = date - dt.timedelta(days=7)
        week_stats = 0
        for item in self.records:
            if (item.date <= date) and (item.date > week_ago):
                week_stats += item.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self, date=None):
        today_get_calories = self.get_today_stats(date)
        remainder = self.limit - today_get_calories
        if remainder <= 0:
            return 'Хватит есть!'
        else:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remainder} кКал'


class CashCalculator(Calculator):
    USD_RATE = 76.0
    EURO_RATE = 91.0
    def get_today_cash_remained(self, currency):
        dict_currency = {
            'rub': 1,
            'usd': self.USD_RATE,
            'eur': self.EURO_RATE
        }
        dict_name = {
            'rub': 'руб',
            'usd': 'USD',
            'eur': 'Euro'
        }
        remainder = round((self.limit - self.get_today_stats()) / dict_currency[currency], 2)
        if remainder == 0:
            return 'Денег нет, держись'
        elif remainder > 0:
            return f'На сегодня осталось {remainder} {dict_name[currency]}'
        else:
            return f'Денег нет, держись: твой долг - {abs(remainder)} {dict_name[currency]}'


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        if not date:
            self.date = dt.date.today()
        else:
            date_format = '%d.%m.%Y'
            self.date = dt.datetime.strptime(date, date_format)
            self.date = dt.datetime.date(self.date)
        self.comment = comment



