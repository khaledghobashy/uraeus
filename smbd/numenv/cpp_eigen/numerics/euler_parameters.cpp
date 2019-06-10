#include "eigen-eigen-323c052e1731/Eigen/Dense"

#include "euler_parameters.hpp"


using namespace Eigen;

Matrix3d A(const Vector4d &P)
{
    double e0 = P(0,0);
    double e1 = P(1,0);
    double e2 = P(2,0);
    double e3 = P(3,0);

    Matrix3d A;

    A(0,0) = pow(e0,2) + pow(e1,2) - pow(e2,2) - pow(e3,2);
    A(0,1) = 2*((e1*e2) - (e0*e3));
    A(0,2) = 2*((e1*e3) + (e0*e2));
    
    A(1,0) = 2*((e1*e2) + (e0*e3));
    A(1,1) = pow(e0,2) - pow(e1,2) + pow(e2,2) - pow(e3,2);
    A(1,2) = 2*((e2*e3) - (e0*e1));
    
    A(2,0) = 2*((e1*e3) - (e0*e2));
    A(2,1) = 2*((e2*e3) + (e0*e1));
    A(2,2) = pow(e0,2) - pow(e1,2) - pow(e2,2) + pow(e3,2);

    return A;
};


MatrixXd B(const Vector4d &P, const Vector3d &u)
{
    Matrix<double, 3, 4> mat;

    double e0 = P(0,0);
    double e1 = P(1,0);
    double e2 = P(2,0);
    double e3 = P(3,0);
    
    double ux = u(0,0);
    double uy = u(1,0);
    double uz = u(2,0);
    
    mat(0,0) = 2*e0*ux + 2*e2*uz - 2*e3*uy ;
    mat(0,1) = 2*e1*ux + 2*e2*uy + 2*e3*uz ;
    mat(0,2) = 2*e0*uz + 2*e1*uy - 2*e2*ux ;
    mat(0,3) = -2*e0*uy + 2*e1*uz - 2*e3*ux ;
    
    mat(1,0) = 2*e0*uy - 2*e1*uz + 2*e3*ux ;
    mat(1,1) = -2*e0*uz - 2*e1*uy + 2*e2*ux ;
    mat(1,2) = 2*e1*ux + 2*e2*uy + 2*e3*uz ;
    mat(1,3) = 2*e0*ux + 2*e2*uz - 2*e3*uy ;
    
    mat(2,0) = 2*e0*uz + 2*e1*uy - 2*e2*ux ;
    mat(2,1) = 2*e0*uy - 2*e1*uz + 2*e3*ux ;
    mat(2,2) = -2*e0*ux - 2*e2*uz + 2*e3*uy ;
    mat(2,3) = 2*e1*ux + 2*e2*uy + 2*e3*uz ;

    return mat;

};

