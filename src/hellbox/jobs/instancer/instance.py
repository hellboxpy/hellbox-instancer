from fontTools import ttLib
from fontTools.varLib import instancer

from hellbox import Chute, Hellbox


class Instance(Chute):
    """Instance pins one or more axes of a variable font to generate a static
    instance. Pass axis tags as keyword arguments.

    Example:
        task.read("*.ttf") >> Instance(wght=700) >> task.write("instances")

    A range can be specified as a tuple to restrict rather than pin an axis:
        Instance(wght=(300, 700))
    """

    def __init__(self, **axes):
        self.axes = axes

    def process(self, file):
        Hellbox.info(f"Generating instance: {file.name}")
        copy = file.copy()
        font = ttLib.TTFont(copy.content_path)
        font = instancer.instantiateVariableFont(font, self.axes)
        font.save(copy.content_path)
        return copy
