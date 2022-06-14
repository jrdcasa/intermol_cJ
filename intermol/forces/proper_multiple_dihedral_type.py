# cJ file
import parmed.unit as units

from intermol.decorators import accepts_compatible_units
from intermol.forces.abstract_dihedral_type import AbstractDihedralType


class ProperMultipleDihedralType(AbstractDihedralType):
    __slots__ = ['phi', 'k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'improper']

    @accepts_compatible_units(None, None, None, None, 
                              k0=units.kilojoules_per_mole,
                              k1=units.kilojoules_per_mole,
                              k2=units.kilojoules_per_mole,
                              k3=units.kilojoules_per_mole,
                              k4=units.kilojoules_per_mole,
                              k5=units.kilojoules_per_mole,
                              k6=units.kilojoules_per_mole,
                              k7=units.kilojoules_per_mole,
                              k8=units.kilojoules_per_mole,
                              improper=None)
    def __init__(self, bondingtype1, bondingtype2, bondingtype3, bondingtype4, 
                 k0=0.0 * units.kilojoules_per_mole,
                 k1=0.0 * units.kilojoules_per_mole,
                 k2=0.0 * units.kilojoules_per_mole,
                 k3=0.0 * units.kilojoules_per_mole,
                 k4=0.0 * units.kilojoules_per_mole,
                 k5=0.0 * units.kilojoules_per_mole,
                 k6=0.0 * units.kilojoules_per_mole,
                 k7=0.0 * units.kilojoules_per_mole,
                 k8=0.0 * units.kilojoules_per_mole,
                 improper=False):
        AbstractDihedralType.__init__(self, bondingtype1, bondingtype2, bondingtype3, bondingtype4, improper)
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.k7 = k7
        self.k8 = k8


class ProperMultipleDihedral(ProperMultipleDihedralType):
    """
    stub documentation
    """
    def __init__(self, atom1, atom2, atom3, atom4, bondingtype1=None, bondingtype2=None, bondingtype3=None, bondingtype4=None, 
                 k0=0.0 * units.kilojoules_per_mole,
                 k1=0.0 * units.kilojoules_per_mole,
                 k2=0.0 * units.kilojoules_per_mole,
                 k3=0.0 * units.kilojoules_per_mole,
                 k4=0.0 * units.kilojoules_per_mole,
                 k5=0.0 * units.kilojoules_per_mole,
                 k6=0.0 * units.kilojoules_per_mole,
                 k7=0.0 * units.kilojoules_per_mole,
                 k8=0.0 * units.kilojoules_per_mole,
                 improper=False):
        self.atom1 = atom1
        self.atom2 = atom2
        self.atom3 = atom3
        self.atom4 = atom4
        ProperMultipleDihedralType.__init__(self, bondingtype1, bondingtype2, bondingtype3, bondingtype4,
                                            k0=k0,
                                            k1=k1,
                                            k2=k2,
                                            k3=k3,
                                            k4=k4,
                                            k5=k5,
                                            k6=k6,
                                            k7=k7,
                                            k8=k8,
                                            improper=improper)