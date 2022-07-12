import math

import pynewtonmath as newton
from Shikimori import SHIKIMORI_PTB
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import ContextTypes


def simplify(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.simplify("{}".format(args[0])))


def factor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.factor("{}".format(args[0])))


def derive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.derive("{}".format(args[0])))


def integrate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.integrate("{}".format(args[0])))


def zeroes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.zeroes("{}".format(args[0])))


def tangent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.tangent("{}".format(args[0])))


def area(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(newton.area("{}".format(args[0])))


def cos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.cos(int(args[0])))


def sin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.sin(int(args[0])))


def tan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.tan(int(args[0])))


def arccos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.acos(int(args[0])))


def arcsin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.asin(int(args[0])))


def arctan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.atan(int(args[0])))


def abs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.fabs(int(args[0])))


def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    message = update.effective_message
    message.reply_text(math.log(int(args[0])))


__mod_name__ = "Math"

SIMPLIFY_HANDLER = DisableAbleCommandHandler("math", simplify, block=False)
FACTOR_HANDLER = DisableAbleCommandHandler("factor", factor, block=False)
DERIVE_HANDLER = DisableAbleCommandHandler("derive", derive, block=False)
INTEGRATE_HANDLER = DisableAbleCommandHandler("integrate", integrate, block=False)
ZEROES_HANDLER = DisableAbleCommandHandler("zeroes", zeroes, block=False)
TANGENT_HANDLER = DisableAbleCommandHandler("tangent", tangent, block=False)
AREA_HANDLER = DisableAbleCommandHandler("area", area, block=False)
COS_HANDLER = DisableAbleCommandHandler("cos", cos, block=False)
SIN_HANDLER = DisableAbleCommandHandler("sin", sin, block=False)
TAN_HANDLER = DisableAbleCommandHandler("tan", tan, block=False)
ARCCOS_HANDLER = DisableAbleCommandHandler("arccos", arccos, block=False)
ARCSIN_HANDLER = DisableAbleCommandHandler("arcsin", arcsin, block=False)
ARCTAN_HANDLER = DisableAbleCommandHandler("arctan", arctan, block=False)
ABS_HANDLER = DisableAbleCommandHandler("abs", abs, block=False)
LOG_HANDLER = DisableAbleCommandHandler("log", log, block=False)

SHIKIMORI_PTB.add_handler(SIMPLIFY_HANDLER)
SHIKIMORI_PTB.add_handler(FACTOR_HANDLER)
SHIKIMORI_PTB.add_handler(DERIVE_HANDLER)
SHIKIMORI_PTB.add_handler(INTEGRATE_HANDLER)
SHIKIMORI_PTB.add_handler(ZEROES_HANDLER)
SHIKIMORI_PTB.add_handler(TANGENT_HANDLER)
SHIKIMORI_PTB.add_handler(AREA_HANDLER)
SHIKIMORI_PTB.add_handler(COS_HANDLER)
SHIKIMORI_PTB.add_handler(SIN_HANDLER)
SHIKIMORI_PTB.add_handler(TAN_HANDLER)
SHIKIMORI_PTB.add_handler(ARCCOS_HANDLER)
SHIKIMORI_PTB.add_handler(ARCSIN_HANDLER)
SHIKIMORI_PTB.add_handler(ARCTAN_HANDLER)
SHIKIMORI_PTB.add_handler(ABS_HANDLER)
SHIKIMORI_PTB.add_handler(LOG_HANDLER)
