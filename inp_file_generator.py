import os

class Calc_Data_Inp:
    """Class Calc_Data_Inp
    
    Parameters:
    **params : **kwargs of {
    molecule : obj Molecule
    method : str
    basis : str
    opt : bool
    freq : bool
    nmr : bool
    cores : int
    memory : int, Gb
    }
    """

    __BASIS_LIST = ['b3lyp']

    def __init__(self, **params):
        self.__molecule = params['molecule']
        self.__method = params['method'].lower()
        self.__basis = params['basis'].lower()
        self.__basis_set_functions = params.get('basis_set_functions', False)
        self.__empiricaldisp = params.get('empiricaldisp', False)
        self.__name = params.get('name', 'Name')
        self.__opt = params.get('opt', False)
        self.__freq = params.get('freq', False)
        self.__nmr = params.get('nmr', False)
        self.__cores = params.get('cores', 4)
        self.__memory = params.get('memory', 4)

    def get_basis_list(self):
        return self.__BASIS_LIST

    @property
    def molecule(self):
        return self.__molecule
    
    @property
    def method(self):
        return self.__method
    
    @property
    def basis(self):
        return self.__basis
    
    @property
    def basis_set_functions(self):
        return self.__basis_set_functions

    @property
    def empiricaldisp(self):
        return self.__empiricaldisp
    
    @property
    def name(self):
        return self.__name
    
    @property
    def opt(self):
        return self.__opt
    
    @property
    def freq(self):
        return self.__freq
    
    @property
    def nmr(self):
        return self.__nmr
    
    @property
    def cores(self):
        return self.__cores
    
    @property
    def memory(self):
        return self.__memory

    def generate_gaussian_inp(self, path, filename):
        """Generate input .log file for gaussian with name - filename in dir - path, and return text of log file"""
        molecule = self.molecule
        method = self.method
        basis = self.basis
        basis_set_functions = self.basis_set_functions
        empiricaldisp = self.empiricaldisp
        name = self.name
        opt = self.opt
        freq = self.freq
        nmr = self.nmr
        cores = self.cores
        memory = self.memory

        basis_functions_place = '\n\n\n'

        if basis not in Calc_Data_Inp.get_basis_list():
            basis = 'gen'
            basis_functions_place = basis_set_functions

        task_line = f'# {method}/{basis} '

        if empiricaldisp:
            task_line += f'empiricaldispersion={empiricaldisp} '
        
        if opt:
            task_line += 'opt '

        if freq:
            task_line += 'freq '

        if nmr:
            task_line += 'nmr=giao '

        atoms_coordinates = []
        atoms = molecule.atoms

        for i in atoms:
            atoms_coordinates.append(f'{i.type} {' '.join(i.coords)}')

        lines = [f'%nprocshared={cores}', f'%mem={memory}GB', task_line, '', f'{name}', '', *atoms_coordinates, '', f'{basis_functions_place}', '\n\n\n']

        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, filename)
        
        with open(filepath, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        
        return lines