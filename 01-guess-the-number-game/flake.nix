{
  description = "Simple Python environment with Nix flakes";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }:
    let
      # Create a function that builds for any system
      forAllSystems = nixpkgs.lib.genAttrs [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
    in {
      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.mkShell {
            buildInputs = [
              pkgs.python312
              pkgs.python312Packages.pip
            ];

            shellHook = ''
              echo "🐍 Python $(python --version)"
              if [ ! -d .venv ]; then
                python -m venv .venv
                echo "🌀 Created local virtualenv .venv"
              fi
              source .venv/bin/activate
              echo "🐍 Virtualenv activated"
            '';
          };
        }
      );
    };
}
