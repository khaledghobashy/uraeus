
import numpy as np
import pandas as pd
from source.solvers.py_numerical_functions import (mirrored, centered, oriented, 
                                                   cylinder_geometry,
                                                   composite_geometry,
                                                   triangular_prism)



class configuration(object):

    def __init__(self):
        self.Rd_rbs_table = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_table = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_table = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_table = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_link_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_link_1 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_link_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_link_1 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_link_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_link_2 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_link_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_link_2 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_link_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_link_3 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_link_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_link_3 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_rocker_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_rocker_1 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_rocker_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_rocker_1 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_rocker_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_rocker_2 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_rocker_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_rocker_2 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rd_rbs_rocker_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pd_rbs_rocker_3 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.Rdd_rbs_rocker_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.Pdd_rbs_rocker_3 = np.array([[0], [0], [0], [0]],dtype=np.float64)
        self.ax1_jcs_bottom_sph_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_bottom_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_bottom_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_bottom_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_middle_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_middle_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_middle_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_upper_1 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_upper_2 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_upper_3 = np.array([[0], [0], [0]],dtype=np.float64)
        self.hps_tripod = np.array([[0], [0], [0]],dtype=np.float64)
        self.s_links_ro = 1
        self.s_rockers_ro = 1                       

    
    @property
    def q(self):
        q = np.concatenate([self.R_rbs_table,self.P_rbs_table,self.R_rbs_link_1,self.P_rbs_link_1,self.R_rbs_link_2,self.P_rbs_link_2,self.R_rbs_link_3,self.P_rbs_link_3,self.R_rbs_rocker_1,self.P_rbs_rocker_1,self.R_rbs_rocker_2,self.P_rbs_rocker_2,self.R_rbs_rocker_3,self.P_rbs_rocker_3])
        return q

    @property
    def qd(self):
        qd = np.concatenate([self.Rd_rbs_table,self.Pd_rbs_table,self.Rd_rbs_link_1,self.Pd_rbs_link_1,self.Rd_rbs_link_2,self.Pd_rbs_link_2,self.Rd_rbs_link_3,self.Pd_rbs_link_3,self.Rd_rbs_rocker_1,self.Pd_rbs_rocker_1,self.Rd_rbs_rocker_2,self.Pd_rbs_rocker_2,self.Rd_rbs_rocker_3,self.Pd_rbs_rocker_3])
        return qd

    def load_from_csv(self,csv_file):
        dataframe = pd.read_csv(csv_file,index_col=0)
        for ind in dataframe.index:
            value = getattr(self,ind)
            if isinstance(value, np.ndarray):
                shape = value.shape
                v = np.array(dataframe.loc[ind],dtype=np.float64)
                v = np.resize(v,shape)
                setattr(self,ind,v)
            else:
                v = dataframe.loc[ind][0]
                setattr(self,ind,v)
        self._set_arguments()

    def _set_arguments(self):
        self.gms_table = triangular_prism(self.hps_upper_1,self.hps_upper_2,self.hps_upper_3,self.s_rockers_ro)
        self.gms_link_1 = cylinder_geometry(self.hps_upper_1,self.hps_middle_1,self.s_links_ro)
        self.gms_link_2 = cylinder_geometry(self.hps_upper_2,self.hps_middle_2,self.s_links_ro)
        self.gms_link_3 = cylinder_geometry(self.hps_upper_3,self.hps_middle_3,self.s_links_ro)
        self.gms_rocker_1 = cylinder_geometry(self.hps_bottom_1,self.hps_middle_1,self.s_rockers_ro)
        self.gms_rocker_2 = cylinder_geometry(self.hps_bottom_2,self.hps_middle_2,self.s_rockers_ro)
        self.gms_rocker_3 = cylinder_geometry(self.hps_bottom_3,self.hps_middle_3,self.s_rockers_ro)
        self.R_rbs_table = self.gms_table.R
        self.P_rbs_table = self.gms_table.P
        self.m_rbs_table = self.gms_table.m
        self.Jbar_rbs_table = self.gms_table.J
        self.R_rbs_link_1 = self.gms_link_1.R
        self.P_rbs_link_1 = self.gms_link_1.P
        self.m_rbs_link_1 = self.gms_link_1.m
        self.Jbar_rbs_link_1 = self.gms_link_1.J
        self.R_rbs_link_2 = self.gms_link_2.R
        self.P_rbs_link_2 = self.gms_link_2.P
        self.m_rbs_link_2 = self.gms_link_2.m
        self.Jbar_rbs_link_2 = self.gms_link_2.J
        self.R_rbs_link_3 = self.gms_link_3.R
        self.P_rbs_link_3 = self.gms_link_3.P
        self.m_rbs_link_3 = self.gms_link_3.m
        self.Jbar_rbs_link_3 = self.gms_link_3.J
        self.R_rbs_rocker_1 = self.gms_rocker_1.R
        self.P_rbs_rocker_1 = self.gms_rocker_1.P
        self.m_rbs_rocker_1 = self.gms_rocker_1.m
        self.Jbar_rbs_rocker_1 = self.gms_rocker_1.J
        self.R_rbs_rocker_2 = self.gms_rocker_2.R
        self.P_rbs_rocker_2 = self.gms_rocker_2.P
        self.m_rbs_rocker_2 = self.gms_rocker_2.m
        self.Jbar_rbs_rocker_2 = self.gms_rocker_2.J
        self.R_rbs_rocker_3 = self.gms_rocker_3.R
        self.P_rbs_rocker_3 = self.gms_rocker_3.P
        self.m_rbs_rocker_3 = self.gms_rocker_3.m
        self.Jbar_rbs_rocker_3 = self.gms_rocker_3.J
        self.ax1_jcs_rev_1 = oriented(self.hps_bottom_1,self.hps_middle_1,self.hps_upper_1)
        self.pt1_jcs_rev_1 = self.hps_bottom_1
        self.ax1_jcs_rev_2 = oriented(self.hps_bottom_2,self.hps_middle_2,self.hps_upper_2)
        self.pt1_jcs_rev_2 = self.hps_bottom_2
        self.ax1_jcs_rev_3 = oriented(self.hps_bottom_3,self.hps_middle_3,self.hps_upper_3)
        self.pt1_jcs_rev_3 = self.hps_bottom_3
        self.ax1_jcs_tripod = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_tripod = self.hps_tripod
        self.ax1_jcs_upper_uni_1 = oriented(self.hps_middle_1,self.hps_upper_1)
        self.ax2_jcs_upper_uni_1 = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_upper_uni_1 = self.hps_upper_1
        self.ax1_jcs_upper_uni_2 = oriented(self.hps_middle_2,self.hps_upper_2)
        self.ax2_jcs_upper_uni_2 = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_upper_uni_2 = self.hps_upper_2
        self.ax1_jcs_upper_uni_3 = oriented(self.hps_middle_3,self.hps_upper_3)
        self.ax2_jcs_upper_uni_3 = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_upper_uni_3 = self.hps_upper_3
        self.pt1_jcs_bottom_sph_1 = self.hps_middle_1
        self.ax1_jcs_bottom_sph_2 = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_bottom_sph_2 = self.hps_middle_2
        self.ax1_jcs_bottom_sph_3 = self.ax1_jcs_bottom_sph_1
        self.pt1_jcs_bottom_sph_3 = self.hps_middle_3
    

