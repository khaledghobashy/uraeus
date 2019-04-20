# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:57:47 2019

@author: khale
"""
import itertools
import sympy as sm

from source.symbolic_classes.abstract_matrices import (reference_frame, vector, 
                                                       quatrenion, zero_matrix,
                                                       A, G, E, matrix_symbol)


class body(reference_frame):
    """A rigid body class.
    
    TODO
    
    Parameters
    ----------
    name : str
        Name of the reference_frame instance. Should mimic a valid python 
        variable name.
    
    Attributes
    ----------
    n : int
        Number of generalized coordinates used to define the body 
        configuration.
    nc : int
        Number of scalar constraint equations (euler-parameters normalization).
    nve : int
        Number of vetor constraint equations (euler-parameters normalization).
    
    A :  A
        The directional cosines matrix that represents the symbolic orientation
        of the body relative to the global_frame. This matrix is function of
        the body orientation parameters e.g. euler-parameters
    R : vector
        A symbolic matrix that represents the location of the body's reference 
        point relative to the global origin.
    Rd : vector
        A symbolic matrix that represents the translational velocity of the
        body's reference point relative to the global origin.
    P : quatrenion
        A symbolic matrix that represents the orientation of the body's 
        reference frame relative to the global frame in terms of 
        euler-parameters.
    Pd : quatrenion
        A symbolic matrix that represents the rotaional velocity of the body's 
        reference frame relative to the global frame in terms of
        euler_parameters time-derivatives.
    
    q : sympy.BlockMatrix
        Blockmatrix containing the position-level coordinates of the body
    qd : sympy.BlockMatrix
        Blockmatrix containing the velocity-level coordinates of the body
        
    normalized_pos_equation : sympy.MatrixExpr
        The normalization equation of the euler-parameters quatrenion at the
        position level.
    normalized_vel_equation : sympy.MatrixExpr
        The normalization equation of the euler-parameters quatrenion at the
        velocity level.
    normalized_acc_equation : sympy.MatrixExpr
        The normalization equation of the euler-parameters quatrenion at the
        acceleration level.
    normalized_jacobian : list (of sympy.MatrixExpr)
        The jacobian of the normalization equation of the euler-parameters 
        quatrenion relative to the vector of euler-parameters.
    
    arguments : list
        A list storing the [`R, P, Rd, Pd`] variables.
    constants : list
        An empty list just for code completeness in development code uses.
        
    """
    
    n   = 7
    nc  = 1
    nve = 1
    
    def __init__(self,name):
        self._name = name
        super().__init__(name)
        
        splited_name = name.split('.')
        self.id_name = ''.join(splited_name[-1])
        self.prefix  = '.'.join(splited_name[:-1])
        self.prefix  = (self.prefix+'.' if self.prefix!='' else self.prefix)
        
        format_ = (self.prefix,self.id_name)
        
        self.R  = vector('%sR_%s'%format_, format_as=r'{%sR_{%s}}'%format_)
        self.P  = quatrenion('%sP_%s'%format_, format_as=r'{%sP_{%s}}'%format_)
        
        self.Rd = vector('%sRd_%s'%format_, format_as=r'{%s\dot{R}_{%s}}'%format_)
        self.Pd = quatrenion('%sPd_%s'%format_, format_as=r'{%s\dot{P}_{%s}}'%format_)
        
        self.Rdd = vector('%sRdd_%s'%format_, format_as=r'{%s\ddot{R}_{%s}}'%format_)
        self.Pdd = quatrenion('%sPdd_%s'%format_, format_as=r'{%s\ddot{P}_{%s}}'%format_)
        
        self.A = A(self.P)
        self.G = G(self.P)
        self.E = E(self.P)
                
        self.normalized_pos_equation = (self.P.T*self.P) - sm.Identity(1)
        self.normalized_vel_equation = zero_matrix(1,1)
        self.normalized_acc_equation = 2*(self.Pd.T*self.Pd)
        self.normalized_jacobian = [zero_matrix(1,3), 2*self.P.T]
                        
        self.m = sm.symbols('m_%s'%self.id_name)
        self.M = self.m*sm.Identity(3)
        self.Jbar = matrix_symbol('%sJbar_%s'%format_, 3, 3, r'{%s\bar{J}_{%s}}'%format_)
        self.J = 4*G(self.P).T*self.Jbar*G(self.P)
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def q(self):
        return sm.BlockMatrix([[self.R],[self.P]])
    @property
    def qd(self):
        return sm.BlockMatrix([[self.Rd],[self.Pd]])
    @property
    def qdd(self):
        return sm.BlockMatrix([[self.Rdd],[self.Pdd]])
        
    @property
    def arguments_symbols(self):
        return [self.R,self.P,self.Rd,self.Pd,self.Rdd,self.Pdd,self.m,self.Jbar]
    @property
    def runtime_symbols(self):
        return [self.R,self.P,self.Rd,self.Pd,self.Rdd,self.Pdd]
    @property
    def constants_symbolic_expr(self):
        return []
    @property
    def constants_numeric_expr(self):
        return []
    @property
    def constants_symbols(self):
        constants_expr = itertools.chain(self.constants_symbolic_expr,
                                         self.constants_numeric_expr)
        return [expr.lhs for expr in constants_expr]
        


class ground(body):
    """A representation of the gorund as a special case of a rigid body class.
    
    TODO
        
    Attributes
    ----------
    n : int
        Number of generalized coordinates used to define the body configuration.
    nc : int
        Number of scalar constraint equations (euler-parameters normalization
        and grounding constraints).
    nve : int
        Number of vetor constraint equations (euler-parameters normalization
        and grounding constraints).
    
    P_ground :  quatrenion
        A symbolic matrix that represents the fixed orientation of ground.
    """
    
    n   = 7
    nc  = 7
    nve = 2
    
    def __new__(cls,*args):
        name = 'ground'
        return super().__new__(cls,name)
    def __init__(self,*args):
        name = 'ground'
        super().__init__(name)
        format_ = (self.prefix,self.id_name)
        self.P_ground = quatrenion('Pg_%s'%self.name,format_as=r'{Pg_{%s}}'%self.name)
        self.M  = matrix_symbol('%sM_%s'%format_,3,3,r'{%sM_{%s}}'%format_)
        self.J = matrix_symbol('%sJ_%s'%format_,3,3,r'{%s{J}_{%s}}'%format_)
        
        self.normalized_pos_equation = sm.BlockMatrix([[self.R], [self.P-self.P_ground]])
        self.normalized_vel_equation = sm.BlockMatrix([[zero_matrix(3,1)],[zero_matrix(4,1)]])
        self.normalized_acc_equation = sm.BlockMatrix([[zero_matrix(3,1)],[zero_matrix(4,1)]])
        self.normalized_jacobian = sm.BlockMatrix([[sm.Identity(3),zero_matrix(3,4)],
                                                   [zero_matrix(4,3),sm.Identity(4)]])
    
    @property
    def arguments_symbols(self):
        return super().arguments_symbols + [self.P_ground,self.M,self.J]
    
    @property
    def constants_numeric_expr(self):
        return []


###############################################################################
###############################################################################


