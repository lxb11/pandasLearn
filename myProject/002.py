#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from datetime import date, timedelta


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


def test01():
    d = {'x': 100, 'y': 200, 'z': 300}
    s1 = pd.Series(d)
    print(s1.index)


def test02():
    l1 = [100, 200, 300]
    l2 = ['x', 'y', 'z']
    s1 = pd.Series(l1, index=l2)
    print(s1.index)


def test03():
    s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
    s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
    s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')
    df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
    # df = pd.DataFrame([s1, s2, s3])
    print(df)


def test04():
    books = pd.read_excel('D:/temp/Books.xlsx', skiprows=3, usecols="C:F",
                          index_col=None, dtype={'ID': str, 'InStore': str, 'Data': str})
    start = date(2018, 1, 1)
    for i in books.index:
        books.at[i, 'ID'] = i + 1
        books.at[i, 'InStore'] = "Yes" if i % 2 == 0 else "No"
        # books['Data'].at[i] = start + timedelta(days=i)
        # books['Data'].at[i] = date(start.year + i, start.month, start.day)
        books.at[i, 'Data'] = add_month(start, i)
    # print(books)
    books.set_index('ID', inplace=True)
    books.to_excel('D:/temp/OutputBooks.xlsx')
    print('Done!')


def main():
    print("---main---")
    test04()


if __name__ == '__main__':
    main()
