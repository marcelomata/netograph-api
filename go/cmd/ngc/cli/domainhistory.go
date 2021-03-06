package cli

import (
	"fmt"
	"io"

	"github.com/netograph/netograph-api/go/proto/ngapi/dsetapi"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

func domainHistoryCommand() *cobra.Command {
	cmd := &cobra.Command{
		Use:     "domainhistory address",
		Aliases: []string{"domhist"},
		Short:   "Retrieve the capture history for an domain",
		Args: func(cmd *cobra.Command, args []string) error {
			if len(args) != 1 {
				return fmt.Errorf("Usage: %s", cmd.Use)
			}
			return nil
		},
		RunE: func(cmd *cobra.Command, args []string) error {
			c, ctx, err := connectDset()
			if err != nil {
				return err
			}

			limit, err := cmd.Parent().PersistentFlags().GetInt64("limit")
			if err != nil {
				return err
			}

			r, err := c.DomainHistory(ctx, &dsetapi.DomainHistoryRequest{
				Dataset: viper.GetString("dset"),
				Domain:  args[0],
				Limit:   limit,
			})
			if err != nil {
				return err
			}
			for {
				v, err := r.Recv()
				if err != nil {
					if err == io.EOF {
						return nil
					}
					return err
				}
				err = Output(cmd, v)
				if err != nil {
					return err
				}
			}
		},
	}
	return cmd
}
