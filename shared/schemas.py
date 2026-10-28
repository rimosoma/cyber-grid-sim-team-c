from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class BusMeasurement(BaseModel):
    vm_pu: Optional[float] = Field(
        None, description="Tensione in p.u. (None se pacchetto perso)"
    )
    va_deg: Optional[float] = Field(
        None, description="Angolo di fase in gradi")
    p_mw: Optional[float] = Field(None, description="Potenza attiva in MW")
    q_mvar: Optional[float] = Field(
        None, description="Potenza reattiva in MVAr"
    )
    status: str = Field("OK", description="OK oppure DROPPED")


class GridRawPayload(BaseModel):
    timestamp: int = Field(
        ..., ge=0, description="Secondo corrente della simulazione"
    )
    buses: Dict[str, BusMeasurement]


class ControlCommandPayload(BaseModel):
    timestamp: int = Field(..., ge=0)
    mode: str = Field(..., pattern="^(MANUAL|AUTO_OPF)$")
    breaker_line_id: Optional[int] = None
    breaker_open: Optional[bool] = None
    redispatch_gen_id: Optional[int] = None
    redispatch_p_mw: Optional[float] = None
