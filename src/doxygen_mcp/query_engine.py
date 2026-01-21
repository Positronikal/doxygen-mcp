import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any

class DoxygenQueryEngine:
    def __init__(self, xml_dir: str):
        self.xml_dir = Path(xml_dir)
        self.index_path = self.xml_dir / "index.xml"
        self.compounds = {}
        self._load_index()

    def _load_index(self):
        if not self.index_path.exists():
            return

        try:
            tree = ET.parse(self.index_path)
            root = tree.getroot()
            for compound in root.findall("compound"):
                name = compound.find("name").text
                kind = compound.get("kind")
                refid = compound.get("refid")
                self.compounds[name] = {
                    "kind": kind,
                    "refid": refid,
                }
        except Exception as e:
            print(f"Error loading index: {e}")

    def query_symbol(self, symbol_name: str) -> Optional[Dict[str, Any]]:
        """Query a class or namespace by name"""
        # Exact match first
        if symbol_name in self.compounds:
            return self._fetch_compound_details(self.compounds[symbol_name]["refid"])

        # Partial match
        for name, info in self.compounds.items():
            if symbol_name.lower() in name.lower():
                return self._fetch_compound_details(info["refid"])

        return None

    def _fetch_compound_details(self, refid: str) -> Dict[str, Any]:
        xml_file = self.xml_dir / f"{refid}.xml"
        if not xml_file.exists():
            return {"error": f"Details file {xml_file} not found"}

        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            compounddef = root.find("compounddef")

            details = {
                "name": compounddef.find("compoundname").text,
                "kind": compounddef.get("kind"),
                "brief": self._get_text_recursive(compounddef.find("briefdescription")),
                "detailed": self._get_text_recursive(compounddef.find("detaileddescription")),
                "members": []
            }

            for section in compounddef.findall("sectiondef"):
                for member in section.findall("memberdef"):
                    details["members"].append({
                        "name": member.find("name").text,
                        "kind": member.get("kind"),
                        "type": self._get_text_recursive(member.find("type")),
                        "args": self._get_text_recursive(member.find("argsstring")),
                        "brief": self._get_text_recursive(member.find("briefdescription")),
                    })

            return details
        except Exception as e:
            return {"error": f"Error parsing {xml_file}: {e}"}

    def _get_text_recursive(self, element) -> str:
        if element is None:
            return ""
        text = element.text or ""
        for child in element:
            text += self._get_text_recursive(child)
            text += child.tail or ""
        return text.strip()

    def list_all_symbols(self, kind_filter: Optional[str] = None) -> List[str]:
        if kind_filter:
            return [name for name, info in self.compounds.items() if info["kind"] == kind_filter]
        return list(self.compounds.keys())
