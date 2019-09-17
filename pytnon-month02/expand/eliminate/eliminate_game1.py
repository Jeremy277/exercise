# !/usr/bin/python
# -*- coding: UTF-8 -*-
# ======================================================================
import os
import sys
import getopt
import time
import random


# ======================================================================
# color output
#
def perror(s):
    print('\033[31m[ERROR] %s\033[31;m' % (s))


def pinfo(s):
    print('\033[32m[INFO] %s\033[32;m' % (s))


def pwarn(s):
    print('\033[33m[WARN] %s\033[33;m' % (s))


# ----------------------------------------------------------
def red():
    print('\033[31mA\033[31;m',)


def yellow():
    print('\033[33mB\033[33;m',)


def blue():
    print('\033[34mC\033[34;m',)


def green():
    print('\033[32mD\033[32;m',)


def one():
    print('\033[31m1\033[31;m',)


def zero():
    print('O',)


def pout(C):
    if C == 'A':
        red()
    elif C == 'B':
        yellow()
    elif C == 'C':
        blue()
    elif C == 'D':
        green()
    else:
        zero()


# ==========================================================
# 4 colors and 3 crash for 5x7 diamonds table
CRASH3_COLS = 7
CRASH3_ROWS = 5
CRASH3_COLORS = ['O', 'A', 'B', 'C', 'D']

CRASH3_DIAMONDS_TABLE = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

CRASH3_DIAMONDS_RESULT = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def crash3_print_colors(table):
    for row in range(0, CRASH3_ROWS, 1):
        for col in range(0, CRASH3_COLS, 1):
            color = table[row][col]
            pout(CRASH3_COLORS[color])
        print('')


def crash3_print_values(table):
    for row in range(0, CRASH3_ROWS, 1):
        for col in range(0, CRASH3_COLS, 1):
            V = table[row][col]
            if V == 1:
                one()
            else:
                zero()
        print('')


def crash3_reset_value(table, V):
    for row in range(0, CRASH3_ROWS, 1):
        for col in range(0, CRASH3_COLS, 1):
            table[row][col] = V


def crash3_init_table(table):
    print("\n----------------------\ncrash3_init_table:\n----------------------")
    color = random.randint(1, 4)
    for row in range(0, CRASH3_ROWS, 1):
        for col in range(0, CRASH3_COLS, 1):
            color = random.randint(1, 4)
            table[row][col] = color


def crash3_on_cell(table, result, row, col):
    if col < CRASH3_COLS - 2:
        (a, b, c) = (table[row][col], table[row][col + 1], table[row][col + 2])
        if a == b and b == c:
            result[row][col] = 0
            result[row][col + 1] = 0
            result[row][col + 2] = 0

    if row < CRASH3_ROWS - 2:
        (a, b, c) = (table[row][col], table[row + 1][col], table[row + 2][col])
        if a == b and b == c:
            result[row][col] = 0
            result[row + 1][col] = 0
            result[row + 2][col] = 0


def crash3_on_trigger(table, result):
    print("\n----------------------\ncrash3_on_trigger:\n----------------------")
    for row in range(0, CRASH3_ROWS, 1):
        for col in range(0, CRASH3_COLS, 1):
            crash3_on_cell(table, result, row, col)


# ==========================================================
# main() entry
if __name__ == "__main__":
    pinfo("crash linked 3 diamonds.\ncopyright by cheungmine, all rights reserved!")

    crash3_init_table(CRASH3_DIAMONDS_TABLE)

    crash3_print_colors(CRASH3_DIAMONDS_TABLE)

    crash3_reset_value(CRASH3_DIAMONDS_RESULT, 1)

    crash3_on_trigger(CRASH3_DIAMONDS_TABLE, CRASH3_DIAMONDS_RESULT)

    crash3_print_values(CRASH3_DIAMONDS_RESULT)
