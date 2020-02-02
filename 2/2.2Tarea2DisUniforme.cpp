/* This program performs a script to plot a continous uniform distribution

   The file dis-uniform.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-uniform.gnu. 
   It will be generated the file dis-uniform.png.

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
    string sa, sb;
    cout << "a = ";
    cin >> sa;
    cout << "b = ";
    cin >> sb;
    
    double a, b;

    try
    {
        a = stod(sa, nullptr);
        b = stod(sb, nullptr);   
    }
    catch(const exception & e)
    {
        cout << "error: invalid arguments" << '\n';
        return 0;
    }
    
    if (a > b)
        swap(a, b);

    ofstream file("dis-uniform.gnu");

    file    << "set term png\n"
            << "set output \'dis-uniform.png\'\n"
            << "# Uniform PDF\n"
            << "uniform(x, a, b) = x < (a < b ? a : b) || x >= (a > b ? a : b) ? 0.0 : 1.0/abs(b - a)\n"
            << "a = " << a << "\n"
            << "b = " << b << "\n" 
            << "mu = (a + b) / 2.0\n"
            << "sigma = (b - a) / sqrt(12.0)\n"
            << "xmin = a - 0.1*(b - a)\n"
            << "xmax = b + 0.1*(b - a)\n"
            << "ymax = 1.1 * uniform(mu, a, b) #No mode\n"
            << "ymin = -0.1 * uniform(mu, a, b)\n"
            << "unset key\n"
            << "set zeroaxis\n"
            << "set xrange [xmin: xmax]\n"
            << "set yrange [ymin: ymax]\n"
            << "set xlabel \"x ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set xtics autofreq\n"
            << "set ytics autofreq\n"
            << "set format x \"%.2f\"\n"
            << "set format y \"%.2f\"\n"
            << "set sample 120+1\n"
            << "set title \"uniform PDF with a = " << a << ", b = " << b << "\n"
            << "plot uniform(x, a, b) with steps";
    
    file.close();
}