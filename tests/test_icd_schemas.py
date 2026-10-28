import pytest
from pydantic import ValidationError
from shared.schemas import ControlCommandPayload, GridRawPayload


def test_valid_grid_payload():
    """Verifica che un messaggio valido della rete elettrica venga accettato."""
    sample_data = {
        "timestamp": 10,
        "buses": {
            "0": {
                "vm_pu": 1.06,
                "va_deg": 0.0,
                "p_mw": -232.4,
                "q_mvar": -16.9,
                "status": "OK",
            },
            "1": {
                "vm_pu": 1.045,
                "va_deg": -4.98,
                "p_mw": -18.3,
                "q_mvar": 29.7,
                "status": "OK",
            },
        },
    }
    payload = GridRawPayload(**sample_data)
    assert payload.timestamp == 10
    assert payload.buses["0"].vm_pu == 1.06


def test_invalid_control_mode_rejected():
    """Verifica che un comando con modalità inventata venga bloccato."""
    bad_command = {
        "timestamp": 5,
        "mode": "HACKER_MODE",  # Deve accettare solo MANUAL o AUTO_OPF
    }
    with pytest.raises(ValidationError):
        ControlCommandPayload(**bad_command)
