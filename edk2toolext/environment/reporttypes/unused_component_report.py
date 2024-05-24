# @file unused_component_report.py
# A report to components that are compiled but not used in the FDF.
##
# Copyright (c) Microsoft Corporation
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
##
"""A report to components that are compiled but not used in the FDF."""
from argparse import ArgumentParser, Namespace
from typing import Tuple

from edk2toollib.database import Edk2DB, Fv, Inf, InstancedInf
from edk2toollib.database import Environment as Env
from sqlalchemy import desc


class UnusedComponentDumpReport:
    """A report to components that are compiled but not used in the FDF."""
    def report_info(self) -> Tuple[str, str]:
        """Returns the report standard information.

        Returns:
            (str, str): A tuple of (name, description)
        """
        return ("unused-components", "Dumps the library instances used by  component.")

    def add_cli_options(self, parserobj: ArgumentParser) -> None:
        """Configure command line arguments for this report."""
        parserobj.add_argument("-e", "--env", dest="env_id", action="store",
                               help="The environment id to generate the report for.")
        parserobj.add_argument("-a", "--ignore-app", dest="ignore_app", action="store_true",
                               help="Ignore application components.")

    def run_report(self, db: Edk2DB, args: Namespace) -> None:
        """Runs the report."""
        with db.session() as session:
            self.env_id = args.env_id or session.query(Env).order_by(desc(Env.date)).first().id

            dsc_components = session.query(InstancedInf).filter(InstancedInf.env==self.env_id).filter(InstancedInf.path==InstancedInf.component).all()
            fdf_components = session.query(InstancedInf).join(Fv.infs).filter(Fv.env == self.env_id).all()

            if args.ignore_app:
                all_libs = session.query(Inf).all()
                all_libs = {lib.path: lib for lib in all_libs}
                dsc_components = filter(lambda lib: "APPLICATION" not in all_libs[lib.path].module_type, dsc_components)

            dsc_components = set([comp.path for comp in dsc_components])
            fdf_components = set([comp.path for comp in fdf_components])

            unused_components = dsc_components - fdf_components

            print("Unused Components:")
            for comp in unused_components:
                print(f'  {comp}')
