/* This program performs a script to plot a continous normal distribution

   The file dis-normal.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-normal.gnu. 
   It will be generated the file dis-normal.png.

   @author: Diego A. Martinez R
   @date:   2/12/2019
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <utility>

using namespace std;

int main(int argc, char* argv[])
{
    string smean, ssigma;
    
    pair<double, double> parameters[3];

    for (int i = 0; i < 3;) {
        double mean, sigma;
        cout << "mean " << i+1 << " = ";
        cin >> smean;
        cout << "sigma " << i+1 << " = ";
        cin >> ssigma;

         try
        {
            mean = stod(smean, nullptr);
            sigma = stod(ssigma, nullptr);   
        }
        catch(const exception & e)
        {
            cout << "error: enter again" << '\n';
            continue;
        }
        
        parameters[i] = { mean, sigma };
        i++;
    }

    ofstream file("dis-normal.gnu");

    file    << "set term png\n"
            << "set output \'dis-normal.png\'\n"
            << "# Normal PDF\n"
            << "normal(x,mu,sigma)=sigma<=0?1/0:invsqrt2pi/sigma*exp(-0.5*((x-mu)/sigma)**2)\n"
            << "invsqrt2pi = 0.398942280401433\n"
            << "mu = 0.0; sigma = 1.0\n"
            << "xmin = mu - 4.0 * sigma\n"
            << "xmax = mu + 4.0 * sigma\n"
            << "mu = 2.0; sigma = 0.5\n"
            << "ymax = 1.1 * normal(mu, mu, sigma) #Mode of normal PDF used\n"
            << "set zeroaxis\n"
            << "set xlabel \"x ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set xtics autofreq\n"
            << "set ytics autofreq\n"
            << "set format x \"%.1f\"\n"
            << "set format y \"%.1f\"\n"
            << "set sample 100\n"
            << "set title \"normal PDF\"\n"
            << "set key left top box\n"
            << "plot [xmin:xmax] [0:ymax]" 
                    << "normal(x, " << parameters[0].first << ", " << parameters[0].second << ") title \"mean = " << parameters[0].first << ", sigma = " << parameters[0].second << "\", \\\n"
                    << "normal(x, " << parameters[1].first << ", " << parameters[1].second << ") title \"mean = " << parameters[1].first << ", sigma = " << parameters[1].second << "\", \\\n"
                    << "normal(x, " << parameters[2].first << ", " << parameters[2].second << ") title \"mean = " << parameters[2].first << ", sigma = " << parameters[2].second << "\n";

    file.close();
}
