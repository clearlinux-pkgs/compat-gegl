#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gegl
Version  : 0.2.0
Release  : 1
URL      : https://download.gimp.org/pub/gegl/0.2/gegl-0.2.0.tar.bz2
Source0  : https://download.gimp.org/pub/gegl/0.2/gegl-0.2.0.tar.bz2
Summary  : Generic Graphics Library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: compat-gegl-bin
Requires: compat-gegl-lib
Requires: compat-gegl-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : intltool
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(babl)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : python
BuildRequires : ruby-dev
Patch1: cve-2012-4433.patch

%description
GEGL-0.2.0
Table of Contents
JavaScript must be enabled in your browser to display the table of
contents.

%package bin
Summary: bin components for the compat-gegl package.
Group: Binaries

%description bin
bin components for the compat-gegl package.


%package dev
Summary: dev components for the compat-gegl package.
Group: Development
Requires: compat-gegl-lib
Requires: compat-gegl-bin
Provides: compat-gegl-devel

%description dev
dev components for the compat-gegl package.


%package lib
Summary: lib components for the compat-gegl package.
Group: Libraries

%description lib
lib components for the compat-gegl package.


%package locales
Summary: locales components for the compat-gegl package.
Group: Default

%description locales
locales components for the compat-gegl package.


%prep
%setup -q -n gegl-0.2.0
%patch1 -p1
pushd ..
cp -a gegl-0.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519230694
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
%configure --disable-static --without-jasper --without-tiff --disable-docs --enable-introspection=no PYTHON=/usr/bin/python2 --without-vala
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --without-jasper --without-tiff --disable-docs --enable-introspection=no PYTHON=/usr/bin/python2 --without-vala   --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1519230694
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
%make_install
%find_lang gegl-0.2

%files
%defattr(-,root,root,-)
%exclude /usr/lib64/haswell/pkgconfig/gegl-0.2.pc

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/gegl
%exclude /usr/bin/haswell/gegl

%files dev
%defattr(-,root,root,-)
/usr/include/gegl-0.2/gegl-buffer-backend.h
/usr/include/gegl-0.2/gegl-buffer-iterator.h
/usr/include/gegl-0.2/gegl-buffer.h
/usr/include/gegl-0.2/gegl-chant.h
/usr/include/gegl-0.2/gegl-color.h
/usr/include/gegl-0.2/gegl-curve.h
/usr/include/gegl-0.2/gegl-enums.h
/usr/include/gegl-0.2/gegl-lookup.h
/usr/include/gegl-0.2/gegl-matrix.h
/usr/include/gegl-0.2/gegl-paramspecs.h
/usr/include/gegl-0.2/gegl-path.h
/usr/include/gegl-0.2/gegl-plugin.h
/usr/include/gegl-0.2/gegl-tile-backend.h
/usr/include/gegl-0.2/gegl-tile-source.h
/usr/include/gegl-0.2/gegl-tile.h
/usr/include/gegl-0.2/gegl-types.h
/usr/include/gegl-0.2/gegl-utils.h
/usr/include/gegl-0.2/gegl-version.h
/usr/include/gegl-0.2/gegl.h
/usr/include/gegl-0.2/opencl/cl.h
/usr/include/gegl-0.2/opencl/cl_d3d10.h
/usr/include/gegl-0.2/opencl/cl_ext.h
/usr/include/gegl-0.2/opencl/cl_gl.h
/usr/include/gegl-0.2/opencl/cl_gl_ext.h
/usr/include/gegl-0.2/opencl/cl_platform.h
/usr/include/gegl-0.2/opencl/gegl-cl-color.h
/usr/include/gegl-0.2/opencl/gegl-cl-init.h
/usr/include/gegl-0.2/opencl/gegl-cl-types.h
/usr/include/gegl-0.2/opencl/gegl-cl.h
/usr/include/gegl-0.2/opencl/opencl.h
/usr/include/gegl-0.2/operation/gegl-operation-area-filter.h
/usr/include/gegl-0.2/operation/gegl-operation-composer.h
/usr/include/gegl-0.2/operation/gegl-operation-composer3.h
/usr/include/gegl-0.2/operation/gegl-operation-filter.h
/usr/include/gegl-0.2/operation/gegl-operation-meta.h
/usr/include/gegl-0.2/operation/gegl-operation-point-composer.h
/usr/include/gegl-0.2/operation/gegl-operation-point-composer3.h
/usr/include/gegl-0.2/operation/gegl-operation-point-filter.h
/usr/include/gegl-0.2/operation/gegl-operation-point-render.h
/usr/include/gegl-0.2/operation/gegl-operation-sink.h
/usr/include/gegl-0.2/operation/gegl-operation-source.h
/usr/include/gegl-0.2/operation/gegl-operation-temporal.h
/usr/include/gegl-0.2/operation/gegl-operation.h
/usr/lib64/haswell/libgegl-0.2.so
/usr/lib64/libgegl-0.2.so
/usr/lib64/pkgconfig/gegl-0.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gegl-0.2/add.so
/usr/lib64/gegl-0.2/bilateral-filter.so
/usr/lib64/gegl-0.2/box-blur.so
/usr/lib64/gegl-0.2/brightness-contrast.so
/usr/lib64/gegl-0.2/buffer-sink.so
/usr/lib64/gegl-0.2/buffer-source.so
/usr/lib64/gegl-0.2/c2g.so
/usr/lib64/gegl-0.2/checkerboard.so
/usr/lib64/gegl-0.2/clear.so
/usr/lib64/gegl-0.2/clone.so
/usr/lib64/gegl-0.2/color-burn.so
/usr/lib64/gegl-0.2/color-dodge.so
/usr/lib64/gegl-0.2/color-temperature.so
/usr/lib64/gegl-0.2/color-to-alpha.so
/usr/lib64/gegl-0.2/color.so
/usr/lib64/gegl-0.2/contrast-curve.so
/usr/lib64/gegl-0.2/convert-format.so
/usr/lib64/gegl-0.2/crop.so
/usr/lib64/gegl-0.2/darken.so
/usr/lib64/gegl-0.2/difference-of-gaussians.so
/usr/lib64/gegl-0.2/difference.so
/usr/lib64/gegl-0.2/display.so
/usr/lib64/gegl-0.2/divide.so
/usr/lib64/gegl-0.2/dropshadow.so
/usr/lib64/gegl-0.2/dst-atop.so
/usr/lib64/gegl-0.2/dst-in.so
/usr/lib64/gegl-0.2/dst-out.so
/usr/lib64/gegl-0.2/dst-over.so
/usr/lib64/gegl-0.2/dst.so
/usr/lib64/gegl-0.2/edge-laplace.so
/usr/lib64/gegl-0.2/edge-sobel.so
/usr/lib64/gegl-0.2/exclusion.so
/usr/lib64/gegl-0.2/exp-combine.so
/usr/lib64/gegl-0.2/fattal02.so
/usr/lib64/gegl-0.2/fractal-explorer.so
/usr/lib64/gegl-0.2/gamma.so
/usr/lib64/gegl-0.2/gaussian-blur.so
/usr/lib64/gegl-0.2/gegl-buffer-load-op.so
/usr/lib64/gegl-0.2/gegl-buffer-save-op.so
/usr/lib64/gegl-0.2/grey.so
/usr/lib64/gegl-0.2/grid.so
/usr/lib64/gegl-0.2/hard-light.so
/usr/lib64/gegl-0.2/introspect.so
/usr/lib64/gegl-0.2/invert.so
/usr/lib64/gegl-0.2/jpg-load.so
/usr/lib64/gegl-0.2/jpg-save.so
/usr/lib64/gegl-0.2/layer.so
/usr/lib64/gegl-0.2/lens-distortion.so
/usr/lib64/gegl-0.2/levels.so
/usr/lib64/gegl-0.2/lighten.so
/usr/lib64/gegl-0.2/load.so
/usr/lib64/gegl-0.2/magick-load.so
/usr/lib64/gegl-0.2/mantiuk06.so
/usr/lib64/gegl-0.2/map-absolute.so
/usr/lib64/gegl-0.2/map-relative.so
/usr/lib64/gegl-0.2/matting-global.so
/usr/lib64/gegl-0.2/mblur.so
/usr/lib64/gegl-0.2/mirrors.so
/usr/lib64/gegl-0.2/mono-mixer.so
/usr/lib64/gegl-0.2/motion-blur.so
/usr/lib64/gegl-0.2/multiply.so
/usr/lib64/gegl-0.2/noise-reduction.so
/usr/lib64/gegl-0.2/noise.so
/usr/lib64/gegl-0.2/nop.so
/usr/lib64/gegl-0.2/opacity.so
/usr/lib64/gegl-0.2/open-buffer.so
/usr/lib64/gegl-0.2/over.so
/usr/lib64/gegl-0.2/overlay.so
/usr/lib64/gegl-0.2/path.so
/usr/lib64/gegl-0.2/pixbuf.so
/usr/lib64/gegl-0.2/pixelize.so
/usr/lib64/gegl-0.2/plus.so
/usr/lib64/gegl-0.2/png-load.so
/usr/lib64/gegl-0.2/png-save.so
/usr/lib64/gegl-0.2/polar-coordinates.so
/usr/lib64/gegl-0.2/posterize.so
/usr/lib64/gegl-0.2/ppm-load.so
/usr/lib64/gegl-0.2/ppm-save.so
/usr/lib64/gegl-0.2/raw-load.so
/usr/lib64/gegl-0.2/rectangle.so
/usr/lib64/gegl-0.2/reinhard05.so
/usr/lib64/gegl-0.2/remap.so
/usr/lib64/gegl-0.2/rgbe-load.so
/usr/lib64/gegl-0.2/rgbe-save.so
/usr/lib64/gegl-0.2/ripple.so
/usr/lib64/gegl-0.2/save-pixbuf.so
/usr/lib64/gegl-0.2/save.so
/usr/lib64/gegl-0.2/screen.so
/usr/lib64/gegl-0.2/snn-mean.so
/usr/lib64/gegl-0.2/soft-light.so
/usr/lib64/gegl-0.2/src-atop.so
/usr/lib64/gegl-0.2/src-in.so
/usr/lib64/gegl-0.2/src-out.so
/usr/lib64/gegl-0.2/src-over.so
/usr/lib64/gegl-0.2/src.so
/usr/lib64/gegl-0.2/stress.so
/usr/lib64/gegl-0.2/stretch-contrast.so
/usr/lib64/gegl-0.2/subtract.so
/usr/lib64/gegl-0.2/svg-huerotate.so
/usr/lib64/gegl-0.2/svg-load.so
/usr/lib64/gegl-0.2/svg-luminancetoalpha.so
/usr/lib64/gegl-0.2/svg-matrix.so
/usr/lib64/gegl-0.2/svg-multiply.so
/usr/lib64/gegl-0.2/svg-saturate.so
/usr/lib64/gegl-0.2/text.so
/usr/lib64/gegl-0.2/threshold.so
/usr/lib64/gegl-0.2/transformops.so
/usr/lib64/gegl-0.2/unsharp-mask.so
/usr/lib64/gegl-0.2/value-invert.so
/usr/lib64/gegl-0.2/vector-fill.so
/usr/lib64/gegl-0.2/vector-stroke.so
/usr/lib64/gegl-0.2/vignette.so
/usr/lib64/gegl-0.2/waves.so
/usr/lib64/gegl-0.2/weighted-blend.so
/usr/lib64/gegl-0.2/write-buffer.so
/usr/lib64/gegl-0.2/xor.so
/usr/lib64/haswell/gegl-0.2/add.so
/usr/lib64/haswell/gegl-0.2/bilateral-filter.so
/usr/lib64/haswell/gegl-0.2/box-blur.so
/usr/lib64/haswell/gegl-0.2/brightness-contrast.so
/usr/lib64/haswell/gegl-0.2/buffer-sink.so
/usr/lib64/haswell/gegl-0.2/buffer-source.so
/usr/lib64/haswell/gegl-0.2/c2g.so
/usr/lib64/haswell/gegl-0.2/checkerboard.so
/usr/lib64/haswell/gegl-0.2/clear.so
/usr/lib64/haswell/gegl-0.2/clone.so
/usr/lib64/haswell/gegl-0.2/color-burn.so
/usr/lib64/haswell/gegl-0.2/color-dodge.so
/usr/lib64/haswell/gegl-0.2/color-temperature.so
/usr/lib64/haswell/gegl-0.2/color-to-alpha.so
/usr/lib64/haswell/gegl-0.2/color.so
/usr/lib64/haswell/gegl-0.2/contrast-curve.so
/usr/lib64/haswell/gegl-0.2/convert-format.so
/usr/lib64/haswell/gegl-0.2/crop.so
/usr/lib64/haswell/gegl-0.2/darken.so
/usr/lib64/haswell/gegl-0.2/difference-of-gaussians.so
/usr/lib64/haswell/gegl-0.2/difference.so
/usr/lib64/haswell/gegl-0.2/display.so
/usr/lib64/haswell/gegl-0.2/divide.so
/usr/lib64/haswell/gegl-0.2/dropshadow.so
/usr/lib64/haswell/gegl-0.2/dst-atop.so
/usr/lib64/haswell/gegl-0.2/dst-in.so
/usr/lib64/haswell/gegl-0.2/dst-out.so
/usr/lib64/haswell/gegl-0.2/dst-over.so
/usr/lib64/haswell/gegl-0.2/dst.so
/usr/lib64/haswell/gegl-0.2/edge-laplace.so
/usr/lib64/haswell/gegl-0.2/edge-sobel.so
/usr/lib64/haswell/gegl-0.2/exclusion.so
/usr/lib64/haswell/gegl-0.2/exp-combine.so
/usr/lib64/haswell/gegl-0.2/fattal02.so
/usr/lib64/haswell/gegl-0.2/fractal-explorer.so
/usr/lib64/haswell/gegl-0.2/gamma.so
/usr/lib64/haswell/gegl-0.2/gaussian-blur.so
/usr/lib64/haswell/gegl-0.2/gegl-buffer-load-op.so
/usr/lib64/haswell/gegl-0.2/gegl-buffer-save-op.so
/usr/lib64/haswell/gegl-0.2/grey.so
/usr/lib64/haswell/gegl-0.2/grid.so
/usr/lib64/haswell/gegl-0.2/hard-light.so
/usr/lib64/haswell/gegl-0.2/introspect.so
/usr/lib64/haswell/gegl-0.2/invert.so
/usr/lib64/haswell/gegl-0.2/jpg-load.so
/usr/lib64/haswell/gegl-0.2/jpg-save.so
/usr/lib64/haswell/gegl-0.2/layer.so
/usr/lib64/haswell/gegl-0.2/lens-distortion.so
/usr/lib64/haswell/gegl-0.2/levels.so
/usr/lib64/haswell/gegl-0.2/lighten.so
/usr/lib64/haswell/gegl-0.2/load.so
/usr/lib64/haswell/gegl-0.2/magick-load.so
/usr/lib64/haswell/gegl-0.2/mantiuk06.so
/usr/lib64/haswell/gegl-0.2/map-absolute.so
/usr/lib64/haswell/gegl-0.2/map-relative.so
/usr/lib64/haswell/gegl-0.2/matting-global.so
/usr/lib64/haswell/gegl-0.2/mblur.so
/usr/lib64/haswell/gegl-0.2/mirrors.so
/usr/lib64/haswell/gegl-0.2/mono-mixer.so
/usr/lib64/haswell/gegl-0.2/motion-blur.so
/usr/lib64/haswell/gegl-0.2/multiply.so
/usr/lib64/haswell/gegl-0.2/noise-reduction.so
/usr/lib64/haswell/gegl-0.2/noise.so
/usr/lib64/haswell/gegl-0.2/nop.so
/usr/lib64/haswell/gegl-0.2/opacity.so
/usr/lib64/haswell/gegl-0.2/open-buffer.so
/usr/lib64/haswell/gegl-0.2/over.so
/usr/lib64/haswell/gegl-0.2/overlay.so
/usr/lib64/haswell/gegl-0.2/path.so
/usr/lib64/haswell/gegl-0.2/pixbuf.so
/usr/lib64/haswell/gegl-0.2/pixelize.so
/usr/lib64/haswell/gegl-0.2/plus.so
/usr/lib64/haswell/gegl-0.2/png-load.so
/usr/lib64/haswell/gegl-0.2/png-save.so
/usr/lib64/haswell/gegl-0.2/polar-coordinates.so
/usr/lib64/haswell/gegl-0.2/posterize.so
/usr/lib64/haswell/gegl-0.2/ppm-load.so
/usr/lib64/haswell/gegl-0.2/ppm-save.so
/usr/lib64/haswell/gegl-0.2/raw-load.so
/usr/lib64/haswell/gegl-0.2/rectangle.so
/usr/lib64/haswell/gegl-0.2/reinhard05.so
/usr/lib64/haswell/gegl-0.2/remap.so
/usr/lib64/haswell/gegl-0.2/rgbe-load.so
/usr/lib64/haswell/gegl-0.2/rgbe-save.so
/usr/lib64/haswell/gegl-0.2/ripple.so
/usr/lib64/haswell/gegl-0.2/save-pixbuf.so
/usr/lib64/haswell/gegl-0.2/save.so
/usr/lib64/haswell/gegl-0.2/screen.so
/usr/lib64/haswell/gegl-0.2/snn-mean.so
/usr/lib64/haswell/gegl-0.2/soft-light.so
/usr/lib64/haswell/gegl-0.2/src-atop.so
/usr/lib64/haswell/gegl-0.2/src-in.so
/usr/lib64/haswell/gegl-0.2/src-out.so
/usr/lib64/haswell/gegl-0.2/src-over.so
/usr/lib64/haswell/gegl-0.2/src.so
/usr/lib64/haswell/gegl-0.2/stress.so
/usr/lib64/haswell/gegl-0.2/stretch-contrast.so
/usr/lib64/haswell/gegl-0.2/subtract.so
/usr/lib64/haswell/gegl-0.2/svg-huerotate.so
/usr/lib64/haswell/gegl-0.2/svg-load.so
/usr/lib64/haswell/gegl-0.2/svg-luminancetoalpha.so
/usr/lib64/haswell/gegl-0.2/svg-matrix.so
/usr/lib64/haswell/gegl-0.2/svg-multiply.so
/usr/lib64/haswell/gegl-0.2/svg-saturate.so
/usr/lib64/haswell/gegl-0.2/text.so
/usr/lib64/haswell/gegl-0.2/threshold.so
/usr/lib64/haswell/gegl-0.2/transformops.so
/usr/lib64/haswell/gegl-0.2/unsharp-mask.so
/usr/lib64/haswell/gegl-0.2/value-invert.so
/usr/lib64/haswell/gegl-0.2/vector-fill.so
/usr/lib64/haswell/gegl-0.2/vector-stroke.so
/usr/lib64/haswell/gegl-0.2/vignette.so
/usr/lib64/haswell/gegl-0.2/waves.so
/usr/lib64/haswell/gegl-0.2/weighted-blend.so
/usr/lib64/haswell/gegl-0.2/write-buffer.so
/usr/lib64/haswell/gegl-0.2/xor.so
/usr/lib64/haswell/libgegl-0.2.so.0
/usr/lib64/haswell/libgegl-0.2.so.0.199.1
/usr/lib64/libgegl-0.2.so.0
/usr/lib64/libgegl-0.2.so.0.199.1

%files locales -f gegl-0.2.lang
%defattr(-,root,root,-)

