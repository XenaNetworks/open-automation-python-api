#: All available test module types.
import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

from .internals.hli_v1.modules.modules_l23.module_l23_base import ModuleL23
from .internals.hli_v1.modules.modules_l23.family_d import (
    MOdin1G3S2PT,
    MOdin1G3S6P,
    MOdin1G3S6P_b,
    MOdin1G3S6PE,
)
from .internals.hli_v1.modules.modules_l23.family_e import (
    MOdin5G4S6PCU,
    MOdin10G3S2PCU,
    MOdin10G3S6PCU,
    MOdin10G5S6PCU,
    MOdin10G5S6PCU_b,
)
from .internals.hli_v1.modules.modules_l23.family_f import (
    MOdin10G1S2P,
    MOdin10G1S2P_b,
    MOdin10G1S2P_c,
    MOdin10G1S2P_d,
    MOdin10G1S2PT,
    MOdin10G1S6P,
    MOdin10G1S6P_b,
    MOdin10G1S12P,
    MOdin10G6S6P_a,
)
from .internals.hli_v1.modules.modules_l23.family_g import (
    MLoki100G3S1P,
    MLoki100G3S1P_b,
    MLoki100G3S1PSE,
    MLoki100G3S1PB,
    MLoki100G3S1PB_b,
)
from .internals.hli_v1.modules.modules_l23.family_h import (
    MLoki100G5S1P,
    MOdin100G3S1P,
)
from .internals.hli_v1.modules.modules_l23.family_i import MLoki100G5S2P
from .internals.hli_v1.modules.modules_l23.family_j import MThor100G5S4P
from .internals.hli_v1.modules.modules_l23.family_k import (
    MThor400G7S1P,
    MThor400G7S1PLE,
)
from .internals.hli_v1.modules.modules_l23.family_l import (
    MThor400G7S1P_b,
    MThor400G7S1P_c,
    MThor400G7S1P_d,
)
from .internals.hli_v1.modules.modules_l23.family_l1 import (
    MFreya800G1S1P_a,
    MFreya800G1S1P_b,
    MFreya800G1S1POSFP_a,
    MFreya800G1S1POSFP_b,
    MFreya800G1S1P_a_g1,
    MFreya800G1S1P_b_g1,
    MFreya800G1S1POSFP_a_g1,
    MFreya800G1S1POSFP_b_g1,
    MFreya800G1S1P_a_g2,
    MFreya800G1S1P_b_g2,
    MFreya800G1S1POSFP_a_g2,
    MFreya800G1S1POSFP_b_g2,
    MFreya800G4S1P_a,
    MFreya800G4S1P_b,
    MFreya800G4S1P_c,
    MFreya800G4S1P_d,
    MFreya800G4S1P_e,
    MFreya800G4S1P_f,
    MFreya800G4S1POSFP_a,
    MFreya800G4S1POSFP_b,
    MFreya800G4S1POSFP_c,
    MFreya800G4S1POSFP_d,
    MFreya800G4S1POSFP_e,
    MFreya800G4S1POSFP_f,
    MFreya800G4S1P_a_g1,
    MFreya800G4S1P_b_g1,
    MFreya800G4S1P_c_g1,
    MFreya800G4S1P_d_g1,
    MFreya800G4S1P_e_g1,
    MFreya800G4S1P_f_g1,
    MFreya800G4S1POSFP_a_g1,
    MFreya800G4S1POSFP_b_g1,
    MFreya800G4S1POSFP_c_g1,
    MFreya800G4S1POSFP_d_g1,
    MFreya800G4S1POSFP_e_g1,
    MFreya800G4S1POSFP_f_g1,
    MFreya800G4S1P_a_g2,
    MFreya800G4S1P_b_g2,
    MFreya800G4S1P_c_g2,
    MFreya800G4S1P_d_g2,
    MFreya800G4S1P_e_g2,
    MFreya800G4S1P_f_g2,
    MFreya800G4S1POSFP_a_g2,
    MFreya800G4S1POSFP_b_g2,
    MFreya800G4S1POSFP_c_g2,
    MFreya800G4S1POSFP_d_g2,
    MFreya800G4S1POSFP_e_g2,
    MFreya800G4S1POSFP_f_g2,
)
from .internals.hli_v1.modules.modules_l23.family_m import MOdin1G3S6PT1RJ45
from .internals.hli_v1.modules.modules_l23.family_n import (
    MOdin40G2S2P,
    MOdin40G2S2PB,
)
from .internals.hli_v1.modules.modules_l23.family_combi import (
    MOdin10G4S2PCombi,
    MOdin10G4S2PCombi_b,
)
from .internals.hli_v1.modules.module_l23ve import ModuleL23VE
from .internals.hli_v1.modules.module_chimera import (
    ModuleChimera,
    MChi100G5S2P,
    MChi100G5S2P_b,
    MChi40G2S2P,
)
from .internals.hli_v1.modules.module_l47 import ModuleL47
from .internals.hli_v1.modules.module_l47ve import ModuleL47VE

import typing

Z10OdinModule = typing.Union[
    "MOdin1G3S2PT",
    "MOdin1G3S6P",
    "MOdin1G3S6P_b",
    "MOdin1G3S6PE",
    "MOdin1G3S6PT1RJ45",
    "MOdin10G4S2PCombi",
    "MOdin10G4S2PCombi_b",
    "MOdin5G4S6PCU",
    "MOdin10G1S2P",
    "MOdin10G1S2P_b",
    "MOdin10G1S2P_c",
    "MOdin10G1S2P_d",
    "MOdin10G1S2PT",
    "MOdin10G1S6P",
    "MOdin10G1S6P_b",
    "MOdin10G1S12P",
    "MOdin10G3S6PCU",
    "MOdin10G3S2PCU",
    "MOdin10G5S6PCU",
    "MOdin10G5S6PCU_b",
    "MOdin10G6S6P_a",
    "MOdin40G2S2P",
    "MOdin40G2S2PB",
    "MOdin100G3S1P",
]

Z100LokiModule = typing.Union[
    "MLoki100G3S1P",
    "MLoki100G3S1P_b",
    "MLoki100G3S1PSE",
    "MLoki100G3S1PB",
    "MLoki100G3S1PB_b",
    "MLoki100G5S1P",
    "MLoki100G5S2P",
]

Z400ThorModule = typing.Union[
    "MThor100G5S4P",
    "MThor400G7S1P",
    "MThor400G7S1PLE",
    "MThor400G7S1P_b",
    "MThor400G7S1P_c",
    "MThor400G7S1P_d",
]

Z800FreyaModule = typing.Union[
    "MFreya800G1S1P_a",
    "MFreya800G1S1P_b",
    "MFreya800G1S1POSFP_a",
    "MFreya800G1S1POSFP_b",
    "MFreya800G4S1P_a",
    "MFreya800G4S1P_b",
    "MFreya800G4S1P_c",
    "MFreya800G4S1P_d",
    "MFreya800G4S1P_e",
    "MFreya800G4S1P_f",
    "MFreya800G4S1POSFP_a",
    "MFreya800G4S1POSFP_b",
    "MFreya800G4S1POSFP_c",
    "MFreya800G4S1POSFP_d",
    "MFreya800G4S1POSFP_e",
    "MFreya800G4S1POSFP_f",
    "MFreya800G1S1P_a_g1",
    "MFreya800G1S1P_b_g1",
    "MFreya800G1S1POSFP_a_g1",
    "MFreya800G1S1POSFP_b_g1",
    "MFreya800G4S1P_a_g1",
    "MFreya800G4S1P_b_g1",
    "MFreya800G4S1P_c_g1",
    "MFreya800G4S1P_d_g1",
    "MFreya800G4S1P_e_g1",
    "MFreya800G4S1P_f_g1",
    "MFreya800G4S1POSFP_a_g1",
    "MFreya800G4S1POSFP_b_g1",
    "MFreya800G4S1POSFP_c_g1",
    "MFreya800G4S1POSFP_d_g1",
    "MFreya800G4S1POSFP_e_g1",
    "MFreya800G4S1POSFP_f_g1",
    "MFreya800G1S1P_a_g2",
    "MFreya800G1S1P_b_g2",
    "MFreya800G1S1POSFP_a_g2",
    "MFreya800G1S1POSFP_b_g2",
    "MFreya800G4S1P_a_g2",
    "MFreya800G4S1P_b_g2",
    "MFreya800G4S1P_c_g2",
    "MFreya800G4S1P_d_g2",
    "MFreya800G4S1P_e_g2",
    "MFreya800G4S1P_f_g2",
    "MFreya800G4S1POSFP_a_g2",
    "MFreya800G4S1POSFP_b_g2",
    "MFreya800G4S1POSFP_c_g2",
    "MFreya800G4S1POSFP_d_g2",
    "MFreya800G4S1POSFP_e_g2",
    "MFreya800G4S1POSFP_f_g2",
]

E100ChimeraModule = typing.Union[
    "MChi100G5S2P",
    "MChi100G5S2P_b",
    "MChi40G2S2P",
]

GenericL23Module = typing.Union[
    Z10OdinModule,
    Z100LokiModule,
    Z400ThorModule,
    Z800FreyaModule,    
]

LegacyModule = typing.Union[
    "ModuleL23VE",
    "ModuleL47",
    "ModuleL47VE",
]

GenericAnyModule = typing.Union[
    GenericL23Module,
    LegacyModule,
    E100ChimeraModule,
]

__all__ = (
    "ModuleL23",

    "LegacyModule",
    "ModuleL23VE",
    "ModuleL47",
    "ModuleL47VE",

    "Z10OdinModule",
    "MOdin1G3S2PT",
    "MOdin1G3S6P",
    "MOdin1G3S6P_b",
    "MOdin1G3S6PE",
    "MOdin1G3S6PT1RJ45",
    "MOdin10G4S2PCombi",
    "MOdin10G4S2PCombi_b",
    "MOdin5G4S6PCU",
    "MOdin10G1S2P",
    "MOdin10G1S2P_b",
    "MOdin10G1S2P_c",
    "MOdin10G1S2P_d",
    "MOdin10G1S2PT",
    "MOdin10G1S6P",
    "MOdin10G1S6P_b",
    "MOdin10G1S12P",
    "MOdin10G3S6PCU",
    "MOdin10G3S2PCU",
    "MOdin10G5S6PCU",
    "MOdin10G5S6PCU_b",
    "MOdin10G6S6P_a",
    "MOdin40G2S2P",
    "MOdin40G2S2PB",
    "MOdin100G3S1P",

    "Z100LokiModule",
    "MLoki100G3S1P",
    "MLoki100G3S1P_b",
    "MLoki100G3S1PSE",
    "MLoki100G3S1PB",
    "MLoki100G3S1PB_b",
    "MLoki100G5S1P",
    "MLoki100G5S2P",

    "Z400ThorModule",
    "MThor100G5S4P",
    "MThor400G7S1P",
    "MThor400G7S1PLE",
    "MThor400G7S1P_b",
    "MThor400G7S1P_c",
    "MThor400G7S1P_d",

    "Z800FreyaModule",
    "MFreya800G1S1P_a",
    "MFreya800G1S1P_b",
    "MFreya800G1S1POSFP_a",
    "MFreya800G1S1POSFP_b",
    "MFreya800G4S1P_a",
    "MFreya800G4S1P_b",
    "MFreya800G4S1P_c",
    "MFreya800G4S1P_d",
    "MFreya800G4S1P_e",
    "MFreya800G4S1P_f",
    "MFreya800G4S1POSFP_a",
    "MFreya800G4S1POSFP_b",
    "MFreya800G4S1POSFP_c",
    "MFreya800G4S1POSFP_d",
    "MFreya800G4S1POSFP_e",
    "MFreya800G4S1POSFP_f",
    "MFreya800G1S1P_a_g1",
    "MFreya800G1S1P_b_g1",
    "MFreya800G1S1POSFP_a_g1",
    "MFreya800G1S1POSFP_b_g1",
    "MFreya800G4S1P_a_g1",
    "MFreya800G4S1P_b_g1",
    "MFreya800G4S1P_c_g1",
    "MFreya800G4S1P_d_g1",
    "MFreya800G4S1P_e_g1",
    "MFreya800G4S1P_f_g1",
    "MFreya800G4S1POSFP_a_g1",
    "MFreya800G4S1POSFP_b_g1",
    "MFreya800G4S1POSFP_c_g1",
    "MFreya800G4S1POSFP_d_g1",
    "MFreya800G4S1POSFP_e_g1",
    "MFreya800G4S1POSFP_f_g1",
    "MFreya800G1S1P_a_g2",
    "MFreya800G1S1P_b_g2",
    "MFreya800G1S1POSFP_a_g2",
    "MFreya800G1S1POSFP_b_g2",
    "MFreya800G4S1P_a_g2",
    "MFreya800G4S1P_b_g2",
    "MFreya800G4S1P_c_g2",
    "MFreya800G4S1P_d_g2",
    "MFreya800G4S1P_e_g2",
    "MFreya800G4S1P_f_g2",
    "MFreya800G4S1POSFP_a_g2",
    "MFreya800G4S1POSFP_b_g2",
    "MFreya800G4S1POSFP_c_g2",
    "MFreya800G4S1POSFP_d_g2",
    "MFreya800G4S1POSFP_e_g2",
    "MFreya800G4S1POSFP_f_g2",

    "E100ChimeraModule",
    "ModuleChimera",
    "MChi100G5S2P",
    "MChi100G5S2P_b",
    "MChi40G2S2P",
    
    "GenericL23Module",
    "GenericAnyModule",
)
