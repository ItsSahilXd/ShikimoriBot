from Shikimori.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
)
from telegram.ext.filters import BaseFilter
from Shikimori import SHIKIMORI_PTB as d, LOGGER
from typing import Optional, Union, List


class ShikimoriHandler:
    def __init__(self, d):
        self._SHIKIMORI_PTB = d

    def command(
        self,
        command: str,
        filters: Optional[BaseFilter] = None,
        admin_ok: bool = False,
        pass_chat_data: bool = False,
        block: bool = False,
        can_disable: bool = True,
        group: Optional[Union[int]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._SHIKIMORI_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            block=block,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._SHIKIMORI_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            block=block,
                            
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[ShikimoriCMD] Loaded handler {command} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._SHIKIMORI_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            block=block,
                            
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._SHIKIMORI_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            block=block,
                            
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[ShikimoriCMD] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        block: bool = False,
        group: Optional[Union[int]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._SHIKIMORI_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, block=block
                        ),
                        group,
                    )
                else:
                    self._SHIKIMORI_PTB.add_handler(
                        MessageHandler(pattern, func, block=block), group
                    )
                LOGGER.debug(
                    f"[ShikimoriMSG] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._SHIKIMORI_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, block=block
                        )
                    )
                else:
                    self._SHIKIMORI_PTB.add_handler(
                        MessageHandler(pattern, func, block=block)
                    )
                LOGGER.debug(
                    f"[ShikimoriMSG] Loaded filter pattern {pattern} for function {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, block: bool = False):
        def _callbackquery(func):
            self._SHIKIMORI_PTB.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, block=block
                )
            )
            LOGGER.debug(
                f"[ShikimoriCALLBACK] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        block: bool = False,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._SHIKIMORI_PTB.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    block=block,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[ShikimoriINLINE] Loaded inlinequery handler with pattern {pattern} for function {func.__name__} | PASSES USER DATA: {pass_user_data} | PASSES CHAT DATA: {pass_chat_data} | CHAT TYPES: {chat_types}"
            )
            return func

        return _inlinequery


Shikimoricmd = ShikimoriHandler(d).command
Shikimorimsg = ShikimoriHandler(d).message
Shikimoricallback = ShikimoriHandler(d).callbackquery
Shikimoriinline = ShikimoriHandler(d).inlinequery
