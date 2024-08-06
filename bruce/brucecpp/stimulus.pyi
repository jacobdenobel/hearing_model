class Stimulus:
    def __init__(self, data: list[float], sampling_rate: int, simulation_duration: float) -> None: ...
    @property
    def data(self) -> list[float]: ...
    @property
    def n_simulation_timesteps(self) -> int: ...
    @property
    def n_stimulation_timesteps(self) -> int: ...
    @property
    def sampling_rate(self) -> int: ...
    @property
    def simulation_duration(self) -> float: ...
    @property
    def stimulus_duration(self) -> float: ...
    @property
    def time_resolution(self) -> float: ...

def from_file(path: str) -> Stimulus: ...
def normalize_db(stim: Stimulus, stim_db: float = ...) -> Stimulus: ...
def ramped_sine_wave(duration: float, simulation_duration: float, sampling_rate: int, rt: float, delay: float, f0: float, db: float) -> Stimulus: ...
