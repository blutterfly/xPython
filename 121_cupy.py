"""
 Please refer to the Installation Guide for details:
      https://docs.cupy.dev/en/stable/install.html
      
      ************************************************************
      
      Traceback (most recent call last):
        File "/home/larry/py/xPython/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/home/larry/py/xPython/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
        File "/home/larry/py/xPython/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-rrcg3l8g/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
        File "/tmp/pip-build-env-rrcg3l8g/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
        File "/tmp/pip-build-env-rrcg3l8g/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 95, in <module>
        File "/tmp/pip-install-pjsorl2e/cupy_9f9127a36c884be18b6e53a9675713fc/install/cupy_builder/cupy_setup_build.py", line 514, in get_ext_modules
          extensions = make_extensions(ctx, compiler, use_cython)
        File "/tmp/pip-install-pjsorl2e/cupy_9f9127a36c884be18b6e53a9675713fc/install/cupy_builder/cupy_setup_build.py", line 363, in make_extensions
          raise Exception('Your CUDA environment is invalid. '
      Exception: Your CUDA environment is invalid. Please check above error log.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
"""