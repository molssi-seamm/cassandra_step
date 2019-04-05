# -*- coding: utf-8 -*-
"""Control parameters for the Cassandra step in a MolSSI flowchart"""

import logging
import molssi_workflow
import pprint

logger = logging.getLogger(__name__)


class Cassandra_Parameters(molssi_workflow.Parameters):
    """The control parameters for Cassandra

    This is a dictionary of Parameters objects, which themselves are
    dictionaries.  You need to replace the 'time' example below with one or
    more definitions of the control parameters for your plugin and application.

    The fields of each Parameter are:

        default: the default value of the parameter, used to reset it
        kind: one of 'integer', 'float', 'string', 'boolean' or 'enum'
        default_units: the default units, used for reseting the value
        enumeration: a tuple of enumerated values. See below for more.
        format_string: a format string for 'pretty' output
        description: a short string used as a prompt in the GUI
        help_text: a longer string to display as help for the user

    While the 'kind' of a variable might be a numeric value, it may still have
    enumerated values, such as 'normal', 'precise', etc. In addition, any
    parameter can be set to a variable of expression, indicated by having '$'
    as the first character in the field.
    """

    parameters = {
        "run_name": {
            "value": 'Run_name',
            "default": 'my_simulation',
            "kind": "string",
            "format_string": "s",
            "enumeration": tuple(),
            "description": "The simulation run name",
            "help_text": ("Files will be named using this name")
        },

        "sim_length": {
            "default": 5000000,
            "kind": "integer",
            "default_units": None,
            "enumeration": tuple(),
            "format_string": "d",
            "description": "Number of steps:",
            "help_text": ("Total number of Monte Carlo steps in a simulation.")
        },

        "sim_length_units": {
            "value": 'Steps',
            "default": 'Steps',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Steps',
                'Sweeps',
            ),
            "description": "Simulation length: ",
            "help_text": ("The units of simulation length")
        },


        "temperature": {
            "default": 450,
            "kind": "float",
            "default_units": "K",
            "enumeration": tuple(),
            "format_string": ".1f",
            "description": "Temperature: ",
            "help_text": ("System temperature")
        },

        "MCF": {
            "value": 'MCF file',
            "default": '/a/b/c/methane.mcf',
            "kind": "string",
            "format_string": "s",
            "enumeration": tuple(),
            "description": "MCF location: ",
            "help_text": ("The file containing a molecule topology")
        },

        "num_mols": {
            "default": 1,
            "kind": "integer",
            "default_units": None,
            "enumeration": tuple(),
            "format_string": "d",
            "description": "Number of molecules: ",
            "help_text": ("Number of molecules")
        },

        "box_shape": {
            "value": 'Cubic',
            "default": 'Cubic',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Cubic',
                'Orthogonal',
                'Triclinic'
            ),
            "description": "Box shape: ",
            "help_text": ("The shape of the simulation box")
        },

        "vdw": {
            "value": 'LJ',
            "default": 'LJ',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'LJ',
                'Mie',
            ),
            "description": "VDW potential ",
            "help_text": ("The functional form for Van der Waals interaction computation")
        },

        "vdw_truncation": {
            "value": 'Standard tail correction',
            "default": 'Standard tail correction',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Standard long tail correction',
                'Spline around cut-off',
                'Truncate potential and shift',
                'Truncate',
            ),
            "description": "VDW potential ",
            "help_text": ("The functional form for Van der Waals interaction computation")
        },

        "vdw_cutoff": {
            "value": 16.0,
            "default": 16.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "VDW cutoff: ",
            "help_text": "The cut-off radius for Van der Waals interactions"
        },

        "electrostatics": {
            "value": 'Ewald',
            "default": 'Ewald',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Ewald',
                'Damped shifted force',
                'Truncate',
                'None',
            ),
            "description": "Electrostatics: ",
            "help_text": ("Method to compute electrostatics")
        },

        "electrostatic_cutoff": {
            "value": 16.0,
            "default": 16.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "Electrostatic cutoff: ",
            "help_text": "The cut-off for electrostatic interactions"
        },


        "cutoff_min": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Minimum cutoff",
            "help_text": "The minimum distance at which energy calculation is computed. If distance between two particles is smaller than this, the move is automatically rejected. "
        },


        "ewald_accuracy": {
            "value": 0.00001,
            "default": 0.00001,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "Ewald sum accuracy: ",
            "help_text": "The accuracy of the ewald recipriocal component",
        },

        "dsf_alpha": {
            "value": 0.2,
            "default": 0.2,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "DSF damping factor: ",
            "help_text": "The damping factor of the DSF method",
        },

        "dim_xx": {
            "value": 40.0,
            "default": 40.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "XX dimension:",
            "help_text": "The XX component of the H matrix"
        },

        "alpha": {
            "value": 10.0,
            "default": 10.0,
            "kind": "float",
            "units": "degrees",
            "default_units": "degrees",
            "format_string": ".2f",
            "description": "Degrees",
            "help_text": "The alpha angle between two basis vectors"
        },

        "translation": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Translation probability",
            "help_text": "Probability of a center-of-mass translation"
        },

        "rotation": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Rotation probability",
            "help_text": "Probability of rotation"
        },

        "angle": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Angle probability",
            "help_text": "Probability of an angle change"
        },

        "dihedral": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Dihedral probability",
            "help_text": "Probability of a dihedral change"
        },

        "regrowth": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Regrowth probability",
            "help_text": "Probability of a molecule regrowth"
        },

        "mixing_rule": {
            "value": 'Lorentz-Berthelot',
            "default": 'Lorentz-Berthelot',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Lorentz-Berthelot',
                'Geometric',
                'Custom',
            ),
            "description": "Electrostatics: ",
            "help_text": ("Method to compute electrostatics")
        },

        "seed_1": {
            "value": "random",
            "default": "random",
            "kind": "integer",
            "units": None,
            "default_units": None,
            "format_string": "",
            "enumeration": ("random",),
            "description": "Random seed 1:",
            "help_text": ("The seed for the random number generator."
                          "'random' means to generate a random integer "
                          "as the seed.")
        },

        "seed_2": {
            "value": "random",
            "default": "random",
            "kind": "integer",
            "units": None,
            "default_units": None,
            "format_string": "",
            "enumeration": ("random",),
            "description": "Random seed 2:",
            "help_text": ("The seed for the random number generator."
                          "'random' means to generate a random integer "
                          "as the seed.")
        },

        "initial_config": {
            "value": 'New configuration',
            "default": 'New configuration',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'New configuration',
                'Read old XYZ file',
                'Restart from checkpoint file',
                'Add molecules to existing configuration',
            ),
            "description": "Initial configuration: ",
            "help_text": ("Specifies the way in which an initial configuration is generated.")
        },

        "initial_config": {
            "value": 'New configuration',
            "default": 'New configuration',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'New configuration',
                'Read old XYZ file',
                'Restart from checkpoint file',
                'Add molecules to existing configuration',
            ),
            "description": "Initial configuration: ",
            "help_text": ("Specifies the way in which an initial configuration is generated.")
        },

        "run_type": {
            "value": 'Equilibration',
            "default": 'Equilibration',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Equilibration',
                'Production',
            ),
            "description": "Run type: ",
            "help_text": ("Equilibration or production.")
        },

        "xyz_freq": {
            "value": "1000",
            "default": "1000",
            "kind": "integer",
            "units": None,
            "default_units": None,
            "format_string": "",
            "enumeration": ("random",),
            "description": "XYZ output frequency",
            "help_text": ("The number of steps after which the current snapshot is output to disk.")
        },

        "thermo_freq": {
            "value": "1000",
            "default": "1000",
            "kind": "integer",
            "units": None,
            "default_units": None,
            "format_string": "",
            "enumeration": ("random",),
            "description": "Property output frequency",
            "help_text": ("The number of steps after which the selected thermodynamic quantities are output to disk.")
        },

        "kappa_insertion": {
            "value": 12,
            "default": 12,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Insertion trials: ",
            "help_text": "The number of trial sites when attempting a molecule insertion. s"
        },

        "kappa_rotation": {
            "value": 12,
            "default": 12,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Rotation trials: ",
            "help_text": "The number of trial rotations when attempting a molecule insertion. s"
        },

        "kappa_dihedral": {
            "value": 12,
            "default": 12,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Dihedral trials: ",
            "help_text": "The number of trial dihedral angles attempted when regrowing a molecule. "
        },

        "Rcut cbmc": {
            "value": 6.0,
            "default": 6.0,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "CBMC cutoff: ",
            "help_text": "The cutoff used to compute the energies of the trial state in a regrowth move. "
        },

    }

    def __init__(self, data=parameters):
        """Initialize the instance, by default from the default
        parameters given in the class"""

        logger.debug('Cassandra_Parameters.__init__')

        super().__init__()

        logger.debug("Initializing Cassandra_Parameters object:")
        logger.debug("\n{}\n".format(pprint.pformat(data)))

        self.update(data)
