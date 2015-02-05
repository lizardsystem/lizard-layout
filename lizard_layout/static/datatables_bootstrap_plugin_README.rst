Hand-copied from
https://github.com/DataTables/Plugins/tree/master/integration/bootstrap

I only copied the latest ('3' in this case) and the images directory.

According to the docs at https://datatables.net/manual/styling/bootstrap, you
should use the '3' css and javascript. The regular datatables css can be
switched off.

Handiest way to copy the files is to do the following::

   $ cd /tmp
   $ git clone git@github.com:DataTables/Plugins.git
   $ cd Plugins/integration/bootstrap/
   $ cp 3 /some/where/static/datatables_bootstrap_plugin/
   $ cp images /some/where/static/datatables_bootstrap_plugin/
