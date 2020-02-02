/* This program performs a script to plot a continous exponential distribution

   The file dis-exponential.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-exponential.gnu. 
   It will be generated the file dis-exponential.png.

   @author: Diego A. Martinez R
   @date:   2/12/2019
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
    string sl;
    cout << "lambda = ";
    cin >> sl;
    
    double lambda;

    try
    {
        lambda = stod(sl, nullptr);   
    }
    catch(const exception & e)
    {
        cout << "error: invalid arguments" << '\n';
        return 0;
    }
    
    ofstream file("dis-exponential.gnu");

    file    << "set term png\n"
            << "set output \'dis-exponential.png\'\n"
            << "# Negative exponential PDF\n"
            << "isint(x) = (int(x) == x)\n"
            << "nexp(x,lambda)=lambda<=0?1/0:x<0?0.0:lambda*exp(-lambda*x)\n"
            << "lambda = " << lambda << "\n"
            << "mu = 1.0 / lambda\n"
            << "sigma = 1.0 / lambda\n"
            << "xmax =  mu + 4.0 * sigma\n"
            << "ymax = lambda #No mode\n"
            << "unset key\n"
            << "set zeroaxis\n"
            << "set xrange [0: xmax]\n"
            << "set yrange [0: ymax]\n"
            << "set xlabel \"x ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set xtics autofreq\n"
            << "set ytics autofreq\n"
            << "set format x \"%.2f\"\n"
            << "set format y \"%.1f\"\n"
            << "set sample 100\n"
            << "set title \"negative exponential (or exponential) PDF with lambda = " << lambda << "\n"
            << "plot nexp(x, lambda)\n";
    file.close();
}