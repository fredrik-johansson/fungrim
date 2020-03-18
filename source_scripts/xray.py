from mpmath import *
from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as patches
from flint import acb, arb, good
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


params= {'text.latex.preamble' : [r'\usepackage{amsmath}']}
rcParams.update(params)

rc('text', usetex=True)

realcolor = []
imagcolor = []
highlightcolor = []
highlightbordercolor = []
branchcutcolor = []
branchcutbordercolor = []

def use_colors():
    # realcolor[:] = [0.2,0.2,0.7]
    # imagcolor[:] = [0.1,0.9,0.1]
    realcolor[:] = [0.1,0.1,0.1]
    imagcolor[:] = [1.0,0.1,0.1]
    highlightcolor[:] = [1.0,1.0,0.0]
    highlightbordercolor[:] = [1.0,0.5,0.0]
    branchcutcolor[:] = [0.2, 0.2, 0.7]
    branchcutbordercolor[:] = [0.0, 0.0, 0.5]

def use_grayscale():
    realcolor[:] = [0.1,0.1,0.1]
    imagcolor[:] = [0.6,0.6,0.6]
    highlightcolor[:] = [0.8,0.8,0.8]
    highlightbordercolor[:] = [0.6,0.6,0.6]
    branchcutcolor[:] = [0.7, 0.7, 0.7]
    branchcutbordercolor[:] = [0.5, 0.5, 0.5]

use_colors()

#spinecolor = (0.333,0.333,0.333)
spinecolor = (0.0,0.0,0.0)

colorcycle = [(0.1,0.2,0.8), (1.0,0.5,0.1), (0.9,0.8,0.2)]
#del colorcycle[1]

directory = [""]

def ticklabel(x):
    if x == int(x):
        return "$" + str(x) + "$"
    if x*2 == int(x*2):
        if x < 0:
            return "$-\\frac{%s}{%s}$" % (str(-int(x*2)), 2)
        else:
            return "$\\frac{%s}{%s}$" % (str(int(x*2)), 2)
    npi = x/pi
    if abs(npi-round(npi)) < 1e-12:
        n = int(round(npi))
        if n == 1:
            return "$\\pi$"
        elif n == -1:
            return "$-\\pi$"
        elif n < 0:
            return "$-%i \\pi$" % (-n)
        else:
            return "$%i \\pi$" % n
    npi = 2.0*x/pi
    if abs(npi-round(npi)) < 1e-12:
        n = int(round(npi))
        if n < 0:
            return "$-\\frac{%i}{%i} \\pi$" % (-n, 2)
        else:
            return "$\\frac{%i}{%i} \\pi$" % (n, 2)
    return "$" + str(x) + "$"

def curveplot(funcs, xaxb, yayb=None, N=400, filename=None, aspectx=1.0, aspecty=1.0, legends=None, decorations=None, xtks=None, ytks=None, xout=0.0, yout=0.0, singularities=[],
        legend_loc='upper right'):
    print(filename)
    xa, xb = xaxb
    xs = linspace(xa-xout, xb+xout, N)
    for v in singularities:
        i = searchsorted(xs, v)
        xs = insert(xs, i, [v-1e-4,v-1e-6,v,v+1e-6,v+1e-4])
    ys = []
    for func in funcs:
        ysf = []
        for x in xs:
            if x in singularities:
                try:
                    v = func(x)
                    assert abs(v) < 1e9
                except:
                    v = nan
                ysf.append(v)
            else:
                ysf.append(func(x))
        ys.append(ysf)

    clf()
    dpi=100

    for scaling in (4.0, 2.0):
        figure(figsize=(aspectx*scaling, aspecty*scaling), dpi=dpi)

        axhline(color="gray", linewidth=0.5, linestyle="--")
        axvline(color="gray", linewidth=0.5, linestyle="--")

        for sing in singularities:
            axvline(sing, color="gray", linewidth=0.5, linestyle="--")

        for i, ysf in enumerate(ys):
            if legends is not None:
                lbl = legends[i]
            else:
                lbl = None
            plot(xs, ysf, label=lbl, zorder=2.0-0.1*i, color=colorcycle[i])

        if decorations is not None:
            decorations()

        #axis("scaled")
        xlim([xa,xb])
        if yayb is not None:
            ya, yb = yayb
            ylim([ya,yb])
        if xtks is not None:
            if len(xtks) == 1:
                xtks = (xtks[0], list(map(ticklabel, xtks[0])))
            xticks(*xtks)
        if ytks is not None:
            if len(ytks) == 1:
                ytks = (ytks[0], list(map(ticklabel, ytks[0])))
            yticks(*ytks)

        if legends is not None:
            if scaling == 4.0:
                legend(loc=legend_loc, prop={'size': 9}, frameon=False, handlelength=1.5)
            else:
                legend(loc=legend_loc, prop={'size': 7}, frameon=False, borderpad=0.08, handlelength=0.75)

        ax = gca()
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor(spinecolor)
        for ticks in ax.xaxis.get_ticklines() + ax.yaxis.get_ticklines():
            ticks.set_color(spinecolor)

        savedpi = 100
        import os
        filename2 = "plot_" + filename
        directory2 = os.path.join(directory[0], filename2)
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        prefix = os.path.join(directory2, filename2)

        if scaling == 4.0:
            savefig(prefix + ".svg", bbox_inches="tight", dpi=4*savedpi, pad_inches=0.02)
            savefig(prefix + ".pdf", bbox_inches="tight", dpi=4*savedpi, pad_inches=0.02)
            savefig(prefix + "_large.png", bbox_inches="tight", dpi=2*savedpi, pad_inches=0.02)
            savefig(prefix + "_medium.png", bbox_inches="tight", dpi=1*savedpi, pad_inches=0.02)
        else:
            savefig(prefix + "_small.png", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)
            savefig(prefix + "_small.svg", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)
            savefig(prefix + "_small.pdf", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)



def xrayplot(func, xaxb, yayb, N, filename, decorations=None, xtks=None, ytks=None, xout=0.0, yout=0.0):
    print(filename)
    xa, xb = xaxb
    ya, yb = yayb
    NX = NY = N
    if xtks is None and xa == -2.0 and xb == 2.0: xtks = ([-2,-1,0,1,2],)
    if ytks is None and ya == -2.0 and yb == 2.0: ytks = ([-2,-1,0,1,2],)
    if xtks is None and xa == -3.0 and xb == 3.0: xtks = ([-2,-1,0,1,2],)
    if ytks is None and ya == -3.0 and yb == 3.0: ytks = ([-2,-1,0,1,2],)
    if xtks is None and xa == -4.0 and xb == 4.0: xtks = ([-4,-2,0,2,4],)
    if ytks is None and ya == -4.0 and yb == 4.0: ytks = ([-4,-2,0,2,4],)
    if xtks is None and xa == -5.0 and xb == 5.0: xtks = ([-4,-2,0,2,4],)
    if ytks is None and ya == -5.0 and yb == 5.0: ytks = ([-4,-2,0,2,4],)
    if xtks is None and xa == -6.0 and xb == 6.0: xtks = ([-6,-3,0,3,6],)
    if ytks is None and ya == -6.0 and yb == 6.0: ytks = ([-6,-3,0,3,6],)
    clf()
    X, Y = meshgrid(linspace(xa-xout,xb+xout,NX), linspace(ya-yout,yb+yout,NY), indexing="ij")
    W = zeros((NX, NY))
    Z = zeros((NX, NY))
    T = zeros((NX, NY))
    for i in range(NX):
        if i in [(i*NX)//10 for i in range(10)]:
            print(i)
        for j in range(NY):
            x = X[i,j]
            y = Y[i,j]
            v = complex(func(complex(x,y)))
            Z[i,j] = v.real
            W[i,j] = v.imag
            T[i,j] = abs(v)

    dpi=100

    for scaling in (4.0, 2.0):
        figure(figsize=(scaling, scaling), dpi=dpi)

        if 1:
            contour(X, Y, T, levels=[1/64., 1/16., 1/4., 1, 4.0, 16., 64.],
                colors=[(c,c,c) for c in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]],
                linewidths=[0.5,0.65,0.75,0.85,0.75,0.65,0.5],
                #linestyles=[":",":",":","-","--","--","--"])
                linestyles=["-","-","-","-","-","-","-"])
        else:
            M = 256
            vals = np.ones((M, 4))
            vals[:, 0] = np.linspace(0.5, 1, M)
            vals[:, 1] = np.linspace(0.5, 1, M)
            vals[:, 2] = np.linspace(0.5, 1, M)
            cmap = ListedColormap(vals)
            TT = tanh(T)**0.5
            pcolormesh(X, Y, TT, cmap=cmap)

        contour1 = contour(X, Y, Z, levels=[0], linewidths=[1.5], colors=[imagcolor])
        contour2 = contour(X, Y, W, levels=[0], linewidths=[1.5], colors=[realcolor])

        if decorations is not None:
            decorations()

        axis("scaled")
        xlim([xa,xb]); ylim([ya,yb])
        if xtks is not None:
            if len(xtks) == 1:
                xtks = (xtks[0], list(map(ticklabel, xtks[0])))
            xticks(*xtks)
        if ytks is not None:
            if len(ytks) == 1:
                ytks = (ytks[0], list(map(ticklabel, ytks[0])))
            yticks(*ytks)

        ax = gca()
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor(spinecolor)
        for ticks in ax.xaxis.get_ticklines() + ax.yaxis.get_ticklines():
            ticks.set_color(spinecolor)

        savedpi = 100
        import os
        filename2 = "xray_" + filename
        directory2 = os.path.join(directory[0], filename2)
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        prefix = os.path.join(directory2, filename2)

        if scaling == 4.0:
            savefig(prefix + ".svg", bbox_inches="tight", dpi=4*savedpi, pad_inches=0.02)
            savefig(prefix + ".pdf", bbox_inches="tight", dpi=4*savedpi, pad_inches=0.02)
            savefig(prefix + "_large.png", bbox_inches="tight", dpi=2*savedpi, pad_inches=0.02)
            savefig(prefix + "_medium.png", bbox_inches="tight", dpi=1*savedpi, pad_inches=0.02)
        else:
            savefig(prefix + "_small.png", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)
            savefig(prefix + "_small.svg", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)
            savefig(prefix + "_small.pdf", bbox_inches="tight", dpi=savedpi, pad_inches=0.01)


def rectangle(xy,w,h,**kwargs):
    gca().add_patch(patches.Rectangle(xy,w,h,zorder=2,**kwargs))

def branchcutline(za,zb,offset=0.05):
    if abs(za.real-zb.real) > abs(za.imag-zb.imag):
        xoff = 0.0
        yoff = offset
        if za.real > zb.real:
            yoff = -yoff
    else:
        xoff = offset
        yoff = 0.0
        if za.imag < zb.imag:
            xoff = -xoff

    plot([za.real, zb.real], [za.imag,zb.imag], linewidth=3, linestyle="-", solid_capstyle="butt", color="white")

    plot([za.real-xoff,zb.real-xoff], [za.imag-yoff,zb.imag-yoff], color=branchcutcolor, linewidth=2, linestyle="-", solid_capstyle="butt")
    plot([za.real+xoff,zb.real+xoff], [za.imag+yoff,zb.imag+yoff], color=branchcutcolor, linewidth=2, linestyle="--", solid_capstyle="butt")

    xoff *= 2
    yoff *= 2
    plot([za.real-xoff,za.real+xoff], [za.imag-yoff,za.imag+yoff], color=branchcutcolor, linewidth=1)
    plot([zb.real-xoff,zb.real+xoff], [zb.imag-yoff,zb.imag+yoff], color=branchcutcolor, linewidth=1)

    # plot([-0.1,0.1],[1,1], color=branchcutcolor, linewidth=1)


def plots(outdir):

    directory[0] = outdir

    curveplot([lambda x: fp.re(mp.ellipk(x)), lambda x: fp.im(mp.ellipk(x))], (-2,2), yayb=(-2,4), N=400, filename="elliptic_k", xout=0.1, yout=0.1, xtks=([-2,0,1,2],),
        singularities=[1])

    curveplot([lambda x: fp.re(mp.ellipe(x)), lambda x: fp.im(mp.ellipe(x))], (-2,2), yayb=(-2,4), N=400, filename="elliptic_e", xout=0.1, yout=0.1, xtks=([-2,0,1,2],),
        singularities=[1])

    _agm = lambda x: complex(acb(x).agm())

    def agm_decor():
        branchcutline(0, -1, offset=0.07)
        branchcutline(-1, -4, offset=0.07)

    curveplot([lambda x: fp.re(_agm(x)), lambda x: fp.im(_agm(x))], (-2,2), yayb=(-0.6,2.1), N=400, filename="agm", xout=0.1, yout=0.1, ytks=([0,1,2],), xtks=([-2,-1,0,1,2],),
        singularities=[-1,0])

    xrayplot(lambda z: complex(acb(z).agm()), (-4,4), (-4,4), 400, "agm", xout=0.1, yout=0.1, decorations=agm_decor)

    curveplot([lambda x: acb(x*1j).modular_lambda().real], (0,4), yayb=(-0.1,1.1), N=400, filename="modular_lambda", xout=0.1, yout=0.1, ytks=([0,0.5,1],), xtks=([0,2,4],))

    curveplot([lambda x: fp.exp(x)], (-4,4), yayb=(-1,7), N=400, filename="exp", xout=0.1, yout=0.1, ytks=([0,2,4,6],), xtks=([-4,-2,0,2,4],))

    curveplot([lambda x: fp.gamma(x)], (-4,4), yayb=(-6,6), N=400, filename="gamma", xout=0.1, yout=0.1, singularities=[-4,-3,-2,-1,0],
        xtks=([-4,-2,0,2,4],), ytks=([-6,-4,-2,0,2,4,6],))

    curveplot([lambda x: fp.re(fp.loggamma(x)), lambda x: fp.im(fp.loggamma(x))],
        (-4,4), yayb=(-7,4), N=2000, filename="log_gamma", xout=0.1, yout=0.1, singularities=[-4,-3,-2,-1,0],
            #legends=["$\\operatorname{Re}(\\log \\Gamma(x))$", "$\\operatorname{Im}(\\log \\Gamma(x))$"],
            legends=["$\\operatorname{Re}$", "$\\operatorname{Im}$"],
            legend_loc="lower right", xtks=([-4,-2,0,2,4],), ytks=([-6,-4,-2,0,2,4],))

    curveplot([lambda s: good(lambda: acb(s).zeta(0.6).real, prec=20),
                lambda s: good(lambda: acb(s).zeta(0.8).real, prec=20),
                    lambda s: good(lambda: acb(s).zeta(1.4).real, prec=20)],
        (-25,11), yayb=[-6.5,6.5], N=400, filename="hurwitz_zeta", xout=0.1, yout=0.1,
            singularities=[1],
            legends=["$\\zeta(s,0.6)$", "$\\zeta(s,0.8)$", "$\\zeta(s,1.4)$"],
            legend_loc='upper center',
            xtks=([-20,-10,0,10],), ytks=([-5,0,5],),)

    def lgamma_decor():
        branchcutline(0, -1, offset=0.07)
        branchcutline(-1, -2, offset=0.07)
        branchcutline(-2, -3, offset=0.07)
        branchcutline(-3, -4, offset=0.07)
        branchcutline(-4, -5, offset=0.07)

    xrayplot(lambda z: complex(good(lambda: acb(2+3j).zeta(z), prec=20, parts=False)), (-5,5), (-5,5), 400, "hurwitz_zeta_param", decorations=lgamma_decor, xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(good(lambda: acb(z).zeta(1+0.5j), prec=20, parts=False)), (-20,20), (-20,20), 400, "hurwitz_zeta", xout=0.1, yout=0.1,
        xtks=([-20,-10,0,10,20],), ytks=([-20,-10,0,10,20],))

    curveplot([lambda x: fp.barnesg(x)],
        (-4,6), yayb=[-0.5,2.5], N=400, filename="barnes_g", xout=0.1, yout=0.1,
            xtks=([-4,-2,0,2,4,6],),
            ytks=([0,1,2],),)

    curveplot([lambda x: fp.sinc(x), lambda x: fp.sinc(pi*x)],
        (-3*pi,3*pi), yayb=[-0.4,1.22], N=400, filename="sinc", xout=0.1, yout=0.1,
            legends=["$\\mathrm{sinc}(x)$", "$\\mathrm{sinc}(\\pi x)$"],
            xtks=([-2*pi,-pi,0,pi,2*pi],), ytks=([0,0.5,1],),)

    def coverup_rectangle(xy,w,h):
        gca().add_patch(patches.Rectangle(xy,w,h,linewidth=0,facecolor=realcolor,zorder=2))

    def elltheta(z, tau):
        return tuple(complex(c) for c in acb(z).modular_theta(tau))

    theta1 = lambda z, tau: elltheta(z, tau)[0]
    theta2 = lambda z, tau: elltheta(z, tau)[1]
    theta3 = lambda z, tau: elltheta(z, tau)[2]
    theta4 = lambda z, tau: elltheta(z, tau)[3]

    def ellzeta(z, tau):
        return complex(acb(z).elliptic_zeta(tau))

    def modlambda(tau):
        if tau.imag < 0.01:
            return 0.0
        return complex(acb(tau).modular_lambda())

    def eisene(k, tau):
        if tau.imag < 0.01:
            return 0.0
        if k == 2:
            return ellzeta(0.5, tau) / fp.zeta(2)
        _, a, b, c = elltheta(0, tau)
        E4 = 0.5*(a**8 + b**8 + c**8)
        E6 = 0.5*(-3*a**8*(b**4+c**4)+b**12+c**12)
        E8 = 0.5*(a**16 + b**16 + c**16)
        if k == 4: return E4
        if k == 6: return E6
        if k == 8: return E8
        if k == 10: return E4 * E6
        if k == 12: return (441*E4**3 + 250*E6**2)/691
        if k == 14: return E4**2 * E6
        if k == 16: return (1617*E4**4 + 2000*E4*E6**2)/3617
        raise ValueError

    #xrayplot(lambda z: complex(acb(z).sinc()), (-8,8), (-8,8), 400, "sinc", xout=0.1, yout=0.1, xtks=([-6,-3,0,3,6],), ytks=([-6,-3,0,3,6],),)
    xrayplot(lambda z: complex(acb(z).sinc()), (-8,8), (-8,8), 400, "sinc", xout=0.1, yout=0.1, xtks=([-2*pi,-pi,0,pi,2*pi],), ytks=([-2*pi,-pi,0,pi,2*pi],),)

    xrayplot(lambda z: complex(acb(z).barnes_g()), (-4,6), (-5,5), 400, "barnes_g", xout=0.1, yout=0.1, xtks=([-4,-2,0,2,4,6],), )

    xrayplot(lambda z: complex(acb(z).log_barnes_g()), (-4,6), (-5,5), 400, "log_barnes_g", xout=0.1, yout=0.1,
        decorations=lgamma_decor, xtks=([-4,-2,0,2,4,6],), )

    xrayplot(lambda z: complex(acb(z).lgamma()), (-5,5), (-5,5), 400, "log_gamma", xout=0.1, yout=0.1,
        decorations=lgamma_decor)

    xrayplot(lambda z: complex(acb(z).digamma()), (-5,5), (-5,5), 400, "digamma", xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(acb(z).polygamma(1)), (-5,5), (-5,5), 400, "trigamma", xout=0.1, yout=0.1)

    xrayplot(lambda tau: 0.0 if tau.imag < 0.13 else theta1(1/3.+0.75j,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_1_tau_b",
        decorations=lambda: coverup_rectangle((-2.5,0),5,0.14), xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))

    xrayplot(lambda tau: 0.0 if tau.imag < 0.13 else theta2(1/3.+0.75j,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_2_tau_b",
        decorations=lambda: coverup_rectangle((-2.5,0),5,0.14), xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))

    xrayplot(lambda tau: 0.0 if tau.imag < 0.13 else theta3(1/3.+0.75j,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_3_tau_b",
        decorations=lambda: coverup_rectangle((-2.5,0),5,0.14), xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))

    xrayplot(lambda tau: 0.0 if tau.imag < 0.13 else theta4(1/3.+0.75j,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_4_tau_b",
        decorations=lambda: coverup_rectangle((-2.5,0),5,0.14), xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))

    xrayplot(lambda tau: theta2(0,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_2_tau", xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))
    xrayplot(lambda tau: theta3(0,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_3_tau", xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))
    xrayplot(lambda tau: theta4(0,tau), (-2.5,2.5), (0,2), 600, "jacobi_theta_4_tau", xout=0.1, yout=0.0, xtks=([-2,-1,0,1,2],), ytks=([0,1,2],))

    w3 = 0.25+0.75j
    xrayplot(lambda z: theta1(z,w3), (-2,2), (-2,2), 400, "jacobi_theta_1_z_c", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta2(z,w3), (-2,2), (-2,2), 400, "jacobi_theta_2_z_c", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta3(z,w3), (-2,2), (-2,2), 400, "jacobi_theta_3_z_c", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta4(z,w3), (-2,2), (-2,2), 400, "jacobi_theta_4_z_c", xout=0.1, yout=0.1)

    xrayplot(lambda z: theta1(z,1j), (-2,2), (-2,2), 400, "jacobi_theta_1_z", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta2(z,1j), (-2,2), (-2,2), 400, "jacobi_theta_2_z", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta3(z,1j), (-2,2), (-2,2), 400, "jacobi_theta_3_z", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta4(z,1j), (-2,2), (-2,2), 400, "jacobi_theta_4_z", xout=0.1, yout=0.1)

    xrayplot(lambda z: theta1(z,0.5j), (-2,2), (-2,2), 400, "jacobi_theta_1_z_b", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta2(z,0.5j), (-2,2), (-2,2), 400, "jacobi_theta_2_z_b", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta3(z,0.5j), (-2,2), (-2,2), 400, "jacobi_theta_3_z_b", xout=0.1, yout=0.1)
    xrayplot(lambda z: theta4(z,0.5j), (-2,2), (-2,2), 400, "jacobi_theta_4_z_b", xout=0.1, yout=0.1)

    fundament_lambda_x = list(linspace(-1,0,80))
    fundament_lambda_y = [0.5*sqrt(1-(2*x+1)**2) for x in fundament_lambda_x]
    x2 = [x + 1.0 for x in fundament_lambda_x]
    y2 = fundament_lambda_y[:]
    fundament_lambda_x = fundament_lambda_x + x2
    fundament_lambda_y = fundament_lambda_y + y2
    fundament_lambda_x = [-1.0] + fundament_lambda_x + [1.0]
    fundament_lambda_y = [2.0] + fundament_lambda_y + [2.0]

    def lambda_decorations():
        coverup_rectangle((-1.5,0),3,0.015)
        coverup_rectangle((-0.05,0),0.1,0.1)
        fill(fundament_lambda_x, fundament_lambda_y, facecolor=highlightcolor, edgecolor=highlightbordercolor, alpha=0.5, linewidth=0.5, zorder=2)

    xrayplot(lambda tau: modlambda(tau), (-1.5,1.5), (0,2), 600, "modular_lambda", xtks=([-1.5,-1,-0.5,0,0.5,1,1.5],), ytks=([0,0.5,1,1.5,2],),
        decorations=lambda_decorations, xout=0.1, yout=0.0)

    fundament_x = list(linspace(-0.5,0.5,100))
    fundament_y = [sqrt(1-x**2) for x in fundament_x]

    fundament_x = [-0.5] + fundament_x + [0.5]
    fundament_y = [2.0] + fundament_y + [2.0]

    def eisenstein_decorations():
        coverup_rectangle((-1,0),2,0.015)
        fill(fundament_x, fundament_y, facecolor=highlightcolor, edgecolor=highlightbordercolor, alpha=0.5, linewidth=0.5, zorder=2)

    xrayplot(lambda tau: eisene(2,tau), (-1,1), (0,2), 600, "eisenstein_e2", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    xrayplot(lambda tau: eisene(4,tau), (-1,1), (0,2), 600, "eisenstein_e4", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    xrayplot(lambda tau: eisene(6,tau), (-1,1), (0,2), 600, "eisenstein_e6", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    xrayplot(lambda tau: eisene(8,tau), (-1,1), (0,2), 600, "eisenstein_e8", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    xrayplot(lambda tau: eisene(10,tau), (-1,1), (0,2), 600, "eisenstein_e10", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    xrayplot(lambda tau: eisene(12,tau), (-1,1), (0,2), 600, "eisenstein_e12", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=eisenstein_decorations, xout=0.1, yout=0.0)

    def zeta_decorations():
        axvspan(0, 1, alpha=0.5, color=highlightcolor)
        axvline(0, alpha=0.5, color=highlightbordercolor, linewidth=0.5)
        axvline(1, alpha=0.5, color=highlightbordercolor, linewidth=0.5)

    xrayplot(lambda z: complex(acb(z).zeta()), (-22,22), (-27,27), 400, "zeta", zeta_decorations, xout=0.1, yout=0.1)

    def plot_elliptic(tau, filename):
        xrayplot(lambda z: complex(acb(z).elliptic_p(tau)), (-1.5,1.5), (-1.5,1.5), 400, filename, xout=0.1, yout=0.1,
            xtks=([-1,0,1],), ytks=([-1,0,1],),
            decorations=lambda: fill([0.0, 1.0, tau.real+1.0, tau.real, 0.0], [0.0, 0.0, tau.imag, tau.imag, 0.0],
                facecolor=highlightcolor, edgecolor=highlightbordercolor, alpha=0.5, linewidth=0.5, zorder=2))


    plot_elliptic(1j, "elliptic_p")
    plot_elliptic(0.5+0.75**0.5*1j, "elliptic_p_2")
    plot_elliptic(-0.8+0.7j, "elliptic_p_3")

    xrayplot(lambda z: complex(acb(z).airy_ai()), (-6,6), (-6,6), 400, "airy_ai", xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(acb(z).airy_bi()), (-6,6), (-6,6), 400, "airy_bi", xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(acb(z).erf()), (-4,4), (-4,4), 400, "erf", xout=0.1, yout=0.1)

    def atan_decor():
        branchcutline(1j, 10j)
        branchcutline(-1j, -10j)

    xrayplot(lambda z: complex(acb(z).log()), (-3,3), (-3,3), 400, "log", xout=0.1, yout=0.1,
        decorations=lambda: branchcutline(0, -10, offset=0.05))

    xrayplot(lambda z: complex(acb(z).sqrt()), (-3,3), (-3,3), 400, "sqrt", xout=0.1, yout=0.1,
        decorations=lambda: branchcutline(0, -10, offset=0.05))


    xrayplot(lambda z: complex(acb(z).atan()), (-2,2), (-2,2), 400, "atan", xout=0.1, yout=0.1, decorations=atan_decor)

    xrayplot(lambda z: complex(acb(z).lambertw()), (-3,3), (-3,3), 400, "lambertw", xout=0.1, yout=0.1,
        decorations=lambda: branchcutline(-exp(-1), -10, offset=0.05))

    xrayplot(lambda z: complex(acb(z).exp()), (-5,5), (-5,5), 400, "exp", xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(acb(z).sin()), (-5,5), (-5,5), 400, "sin", xout=0.1, yout=0.1)

    xrayplot(lambda z: complex(acb(z).gamma()), (-5,5), (-5,5), 400, "gamma", xout=0.1, yout=0.1)

    def coverup_rectangle(xy,w,h):
        gca().add_patch(patches.Rectangle(xy,w,h,linewidth=0,facecolor=realcolor,zorder=2))

    def modj(z):
        if z.imag < 0.03:
            return 0.0
        return complex(acb(z).modular_j())/1728.0

    fundament_x = list(linspace(-0.5,0.5,100))
    fundament_y = [sqrt(1-x**2) for x in fundament_x]

    fundament_x = [-0.5] + fundament_x + [0.5]
    fundament_y = [2.0] + fundament_y + [2.0]

    def modular_j_decorations():
        coverup_rectangle((-1,0),2,0.04)
        coverup_rectangle((-1,0),0.1,0.1)
        coverup_rectangle((-0.1,0),0.2,0.1)
        coverup_rectangle((0.9,0),0.1,0.1)
        fill(fundament_x, fundament_y, facecolor=highlightcolor, edgecolor=highlightbordercolor, alpha=0.5, linewidth=0.5, zorder=2)

    xrayplot(modj, (-1,1), (0,2), 600, "modular_j", xtks=([-1,-0.5,0,0.5,1],), ytks=([0,0.5,1,1.5,2],),
        decorations=modular_j_decorations, xout=0.1, yout=0.0)

