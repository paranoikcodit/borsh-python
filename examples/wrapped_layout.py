from borsh import types
from solders.pubkey import Pubkey


class pubkey(types.WrappedLayout):
    _inner_type = types.fixed_array(types.u8, 32)

    @staticmethod
    def _encode(obj: Pubkey) -> list[int]:
        return list(bytes(obj))

    @staticmethod
    def _decode(obj: list[int]) -> Pubkey:
        return Pubkey.from_bytes(bytes(obj))
