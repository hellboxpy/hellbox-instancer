from unittest.mock import MagicMock, patch

from hellbox.jobs.instancer import Instance


class TestInstance:
    def test_init(self):
        assert Instance(wght=700)

    def test_init_stores_axes(self):
        i = Instance(wght=700, wdth=100)
        assert i.axes == {"wght": 700, "wdth": 100}

    def test_process(self):
        file = MagicMock()
        copy = MagicMock()
        file.copy.return_value = copy
        hinted_font = MagicMock()

        with (
            patch("hellbox.jobs.instancer.instance.ttLib") as mock_ttlib,
            patch("hellbox.jobs.instancer.instance.instancer") as mock_instancer,
        ):
            mock_font = MagicMock()
            mock_ttlib.TTFont.return_value = mock_font
            mock_instancer.instantiateVariableFont.return_value = hinted_font

            result = Instance(wght=700).process(file)

        mock_ttlib.TTFont.assert_called_once_with(copy.content_path)
        mock_instancer.instantiateVariableFont.assert_called_once_with(
            mock_font, {"wght": 700}
        )
        hinted_font.save.assert_called_once_with(copy.content_path)
        assert result is copy
