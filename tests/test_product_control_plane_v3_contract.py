from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "brand-kits" / "mvx-hermes-agent" / "v3" / "product-control-plane.manifest.json"
CATALOG = ROOT / "brand-kits" / "mvx-hermes-agent" / "v3" / "mockup_catalog.json"

def test_product_control_plane_v3_manifest_is_fail_closed_until_brand_is_approved():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["schema_version"] == "3.0"
    assert data["development"]["method"] == "tdd"
    assert data["development"]["definition_of_done_hard_gate"] is True
    assert data["implementation_gate"] == "blocked"
    assert data["mockups"]["target_minimum"] >= 30
    assert data["mockups"]["approved"] < data["mockups"]["target_minimum"]

def test_product_control_plane_v3_has_30_planned_mock_ids():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    items = [item for group in data["groups"] for item in group["items"]]
    assert len(items) == 30
    assert len(set(item.split()[0] for item in items)) == 30
