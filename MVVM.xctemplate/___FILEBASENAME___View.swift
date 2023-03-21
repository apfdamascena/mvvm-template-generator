//
//  ___FILENAME___
//  ___PROJECTNAME___
//
//  Created by ___FULLUSERNAME___ on ___DATE___.
//  ___COPYRIGHT___
//

import SwiftUI

struct ___VARIABLE_ModuleName___View: View, ___VARIABLE_ModuleName___ViewProtocol {

    @ObservedObject private var viewModel: ___VARIABLE_ModuleName___ViewModelProtocol?

    init(viewModel: ___VARIABLE_ModuleName___ViewModelProtocol = ___VARIABLE_ModuleName___ViewModel()){
        self.viewModel = viewModel
    }
        
    var body: some View {
        Text("Hello World")
    }

}

struct ___VARIABLE_ModuleName____Previews: PreviewProvider {
    static var previews: some View {
        ___VARIABLE_ModuleName___View()
    }
}