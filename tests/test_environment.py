import pathlib
import py_compile
import helics as h
import pandapower as pp
import pandapower.networks as pn
import pytest

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent


def test_repository_folders_exist():
    """Verifica che nessuno abbia cancellato o rinominato per sbaglio le cartelle dei WP."""
    required_folders = [
        "config",
        "docs",
        "shared",
        "wp1_power_grid",
        "wp2_scada_network",
        "wp3_attack_generator",
        "wp4_defense_module",
        "wp5_control_center",
        "wp6_orchestrator_db",
        "wp7_dashboard",
    ]
    for folder in required_folders:
        assert (
            ROOT_DIR / folder
        ).is_dir(), f"Cartella mancante: {folder}"


def test_all_python_files_syntax():
    """Controlla che tutti i file .py nel progetto siano privi di errori di sintassi."""
    py_files = list(ROOT_DIR.rglob("*.py"))
    assert len(py_files) > 0, "Nessun file Python trovato!"
    for py_file in py_files:
        if ".git" in py_file.parts or "venv" in py_file.parts:
            continue
        # Se c'è un errore di sintassi, py_compile solleva un'eccezione e fa fallire il test
        py_compile.compile(str(py_file), doraise=True)


def test_ieee14_power_flow_baseline():
    """Verifica che pandapower carichi la rete IEEE 14-bus e risolva il Power Flow."""
    net = pn.case14()
    assert len(net.bus) == 14, "La rete IEEE 14-bus deve avere 14 nodi"
    pp.runpp(net)
    assert net.converged is True, "Il calcolo del Power Flow non è converso!"
    # Verifica che le tensioni siano in un range fisicamente sensato (0.8 - 1.2 p.u.)
    assert (net.res_bus.vm_pu > 0.8).all() and (net.res_bus.vm_pu < 1.2).all()


def test_helics_version():
    """Verifica che la libreria di co-simulazione HELICS risponda correttamente."""
    version = h.helicsGetVersion()
    assert version is not None and len(version) > 0
