"""Verifica a identidade pública e a compatibilidade da marca DiakoLight."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BrandingTest(unittest.TestCase):
    def test_android_uses_application_name_resource(self):
        source = (ROOT / "app/app/src/main/java/com/diakolight/ui/CockpitApp.kt").read_text(encoding="utf-8")
        self.assertIn("Text(stringResource(R.string.app_name))", source)

    def test_desktop_display_name_and_settings_compatibility(self):
        variables = (ROOT / "qlcplus/variables.cmake").read_text(encoding="utf-8")
        main = (ROOT / "qlcplus/qmlui/main.cpp").read_text(encoding="utf-8")
        self.assertIn('set(APPNAME "DiakoLight")', variables)
        self.assertIn('setApplicationName("Q Light Controller Plus")', main)
        self.assertIn("setApplicationDisplayName(APPNAME)", main)

    def test_windows_installer_and_shortcut(self):
        installer = (ROOT / "qlcplus/platforms/windows/qlcplus5Qt6.nsi").read_text(encoding="utf-8")
        self.assertIn('Name "DiakoLight"', installer)
        self.assertIn(r"\DiakoLight.lnk", installer)
        self.assertNotIn('"Q Light Controller Plus"', installer)
        self.assertIn('"Software\\Classes\\QLightControllerPlus.Document"', installer)
        self.assertIn("$INSTDIR\\qlcplus5.exe", installer)


if __name__ == "__main__":
    unittest.main()
