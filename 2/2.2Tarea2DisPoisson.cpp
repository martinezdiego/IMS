/* This program performs a script to plot a discrete poisson distribution

   The file dis-poisson.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-poisson.gnu. 
   It will be generated the file dis-poisson.png.

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
    
    ofstream file("dis-poisson.gnu");

    file    << "set term png\n"
            << "set output \'dis-poisson.png\'\n"
            << "# Poisson PDF\n"
            << "isint(x) = (int(x) == x)\n"
            << "poisson(x, mu) = mu <= 0? 1/0 :!isint(x) ? 1/0 : x < 0 ? 0.0 : exp(x*log(mu)-lgamma(x+1)-mu)\n"
            << "mu = " << lambda << "\n"
            << "sigma = sqrt(mu)\n" 
            << "xmin = int(mu - " << lambda << " * sigma)\n"
            << "xmin = xmin < -1 ? -1 : xmin\n"
            << "xmax = int(mu + 4.0 * sigma)\n"
            << "ymax = 1.1 * poisson(mu, mu) #mode of poisson PDF used\n"
            << "unset key\n"
            << "set zeroaxis\n"
            << "set xrange [xmin : xmax]\n"
            << "set yrange [0 : ymax]\n"
            << "set xlabel \"k ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set ytics 0, ymax / 10, ymax\n"
            << "set format x \"%2.0f\"\n"
            << "set format y \"%3.2f\"\n"
            << "set sample (xmax - xmin) + 1\n"
            << "set title \"poisson PDF with mu = 4.0\"\n"
            << "plot poisson(x, mu) with impulses\n";
    
    file.close();
}