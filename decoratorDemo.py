""" Decorator Pattern for a attachment system for guns example"""


# Interface
class Weapon:
    def aim(self) -> str:
        pass

    def shoot(self) -> str:
        pass


# Concrete class
class baseWeapon(Weapon):
    def aim(self) -> str:
        return "aiming"

    def shoot(self) -> str:
        return "Pew"


# Concrete component
class rifle(baseWeapon):
    def ammunition(self) -> str:
        return "big bullet"


# Concrete component
class pistol(baseWeapon):
    def ammunition(self) -> str:
        return "small bullet"


# Main Decorator
class weaponDecorator(baseWeapon):
    def __init__(self, weapon):
        self._weapon = weapon

    def aim(self) -> str:
        return self._weapon.aim()

    def shoot(self) -> str:
        return self._weapon.shoot()

    def __getattr__(self, name):
        return getattr(self._weapon, name)


class ScopeDecorator(weaponDecorator):
    def aim(self) -> str:
        return f"{self._weapon.aim()} with precision"


class SilencerDecorator(weaponDecorator):
    def shoot(self) -> str:
        return f"{self._weapon.shoot()} quietly"


class LaserSightDecorator(weaponDecorator):
    def aim(self) -> str:
        return f"{self._weapon.aim()} with laser dot"


class ExtendedMagazineDecorator(weaponDecorator):
    def shoot(self) -> str:
        return f"{self._weapon.shoot()} Pew Pew Pew (multiple shots)"


if __name__ == "__main__":
    print()

    simplePistol = pistol()
    print("Pistol:")
    print(f"Aim: {simplePistol.aim()}")
    print(f"Shoot: {simplePistol.shoot()}")
    print(f"Bullet: {simplePistol.ammunition()}")
    print()

    tacticalPistol = LaserSightDecorator(SilencerDecorator(pistol()))
    print("Pistol:")
    print(f"Aim: {tacticalPistol.aim()}")
    print(f"Shoot: {tacticalPistol.shoot()}")
    print(f"Bullet: {tacticalPistol.ammunition()}")
    print()

    chadRifle = LaserSightDecorator(
        SilencerDecorator(ExtendedMagazineDecorator(ScopeDecorator(rifle())))
    )
    print("Rifle:")
    print(f"Aim: {chadRifle.aim()}")
    print(f"Shoot: {chadRifle.shoot()}")
    print(f"Bullet: {chadRifle.ammunition()}")
    print()
