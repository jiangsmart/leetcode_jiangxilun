# coding=utf-8


def judge(history, now_y):
    if history == []:
        return True
    now_x = len(history)
    for x, y in enumerate(history):
        if y == now_y or (now_y - y) == (now_x - x) or (now_y - y) == -(now_x - x):
            return False
    return True


def fun(history, solution, N):
    for j in range(N):
        if judge(history, j):  # 依次判断j和当前history是否冲突
            h = history + [j]  # 注意不要用history.append(),改变history会影响循环的后续
            if len(h) == N:  # history长度为8时把解append进入solution
                solution.append(h[:])
            elif len(h) < N:
                fun(h[:], solution, N)


def printQueen(solutions, N):
    outs = []
    for s in solutions:
        out=[]
        for i in s:
            #print i
            row = ['.' for j in range(N)]
            row[i] = 'Q'
            r="".join(row)
            out.append(r)
        outs.append(out)
    return outs


solution = []
history = []
N = 8
fun(history, solution, N)
#print solution
printQueen(solution,N)


# -*- coding: utf-8 -*-
# python默认为ascii编码，中文编码可以用utf-8
import random


# 随机模块

# def conflict(state, col):
#     # 冲突函数，row为行，col为列
#     row = len(state)
#     for i in range(row):
#         if abs(state[i] - col) in (0, row - i):  # 重要语句
#             return True
#     return False
#
#
# def queens(num=8, state=()):
#     # 生成器函数
#     for pos in range(num):
#         if not conflict(state, pos):
#             if len(state) == num - 1:
#                 yield (pos,)
#             else:
#                 for result in queens(num, state + (pos,)):
#                     print result
#                     yield (pos,) + result
#
#
# def queenprint(solution):
#     # 打印函数
#     def line(pos, length=len(solution)):
#         return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
#
#     for pos in solution:
#         print line(pos)

# for solution in list(queens(8)):
#     print solution
#
# print '  total number is ' + str(len(list(queens())))
# print '  one of the range is:\n'
# queenprint(random.choice(list(queens())))
